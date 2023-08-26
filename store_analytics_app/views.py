import json
import math
from random import randrange
import random
from django.http import JsonResponse
from django.shortcuts import render
from .models import Store, ExternalEvent
from .models import Store, RetentionData

from .models import PurchaseData, SalesData

def home_view(request):
    return render(request, 'home.html')

def sales_and_purchase_demand_view(request):
    # Aquí debes obtener y procesar los datos de compra y venta
    # Supongamos que obtienes los datos de las tablas PurchaseData y SalesData
    peak_data = [
        {"date": "2023-08-15", "affected_commerce": "Comercio A"},
        {"date": "2023-08-17", "affected_commerce": "Comercio B"},
        {"date": "2023-08-17", "affected_commerce": "Comercio B"},
        {"date": "2023-08-17", "affected_commerce": "Comercio E"},
        {"date": "2023-08-17", "affected_commerce": "Comercio E"},
        {"date": "2023-08-17", "affected_commerce": "Comercio A"},
        {"date": "2023-08-17", "affected_commerce": "Comercio D"},
        {"date": "2023-08-17", "affected_commerce": "Comercio D"},
        {"date": "2023-08-17", "affected_commerce": "Comercio D"},
        {"date": "2023-08-17", "affected_commerce": "Comercio A"},
        {"date": "2023-08-17", "affected_commerce": "Comercio C"},
        {"date": "2023-08-17", "affected_commerce": "Comercio F"},
    ]

    # Renderizar la plantilla con el gráfico
    return render(request, 'sales_and_purchase_demand.html', {'peak_data': peak_data})

def external_events_view(request):
    # Lógica para obtener datos de tiendas y eventos externos
    stores = Store.objects.all()  # Obtén todas las tiendas
    external_events = ExternalEvent.objects.all()  # Obtén todos los eventos externos
    
    context = {
        'stores': stores,
        'external_events': external_events,
    }
    
    return render(request, 'external_events.html', context)

def retention_rate_view(request):
    # Lógica para obtener datos de tiendas y tasas de retención
    stores = Store.objects.all()  # Obtén todas las tiendas
    retention_rates = RetentionData.objects.all()  # Obtén todas las tasas de retención
    
    context = {
        'stores': stores,
        'retention_rates': retention_rates,
    }
    
    return render(request, 'retention_rate.html', context)

def outlier_summary_view(request):
    # Lógica para obtener información resumida sobre los tipos de outliers
    context = {
        # Datos relevantes para el resumen de outliers
    }
    
    return render(request, 'outlier_summary.html', context)

def kpi_view(request):
    # Lógica para obtener indicadores clave de rendimiento
    context = {
        # Datos relevantes para los KPIs
    }
    
    return render(request, 'kpi.html', context)


def get_chart(_request):

    colors = ['blue', 'orange', 'red', 'black', 'yellow', 'green', 'magenta', 'lightblue', 'purple', 'brown']
    random_color = colors[randrange(0, (len(colors)-1))]

    serie = []
    counter = 0

    while (counter < 7):
        serie.append(randrange(100, 400))
        counter += 1

    chart = {
        'title': {
            'text': 'Referer of a Website',
            'subtext': 'Fake Data',
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'item'
        },
        'legend': {
            'orient': 'vertical',
            'left': 'left'
        },
        'series': [
            {
            'name': 'Access From',
            'type': 'pie',
            'radius': '50%',
            'data': [
                { 'value': 1048, 'name': 'Search Engine' },
                { 'value': 735, 'name': 'Direct' },
                { 'value': 580, 'name': 'Email' },
                { 'value': 484, 'name': 'Union Ads' },
                { 'value': 300, 'name': 'Video Ads' }
            ],
            'emphasis': {
                'itemStyle': {
                'shadowBlur': 10,
                'shadowOffsetX': 0,
                'shadowColor': 'rgba(0, 0, 0, 0.5)'
                }
            }
            }
        ]
    }

    return JsonResponse(chart)

def demand_trends_chart(_request):
    # Obtén los datos de compras y ventas desde tus modelos
    purchases = PurchaseData.objects.all()  # Reemplaza con la forma correcta de obtener los datos
    sales = SalesData.objects.all()  # Reemplaza con la forma correcta de obtener los datos

    # Procesa los datos para prepararlos para ECharts
    data = [['Date', 'Compras', 'Ventas']]
    for purchase in purchases:
        data.append([purchase.date.strftime('%Y-%m-%d'), purchase.amount, None])
    for sale in sales:
        data.append([sale.date.strftime('%Y-%m-%d'), None, sale.amount])

    # Ordena los datos por fecha
    data.sort(key=lambda x: x[0])

    # Crea el JsonResponse
    chart = {
        'legend': {},
        'tooltip': {
            'trigger': 'axis',
            'showContent': False
        },
        'dataset': {
            'source': [
            ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
            ['Milk Tea', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
            ['Matcha Latte', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7]
            ]
        },
        'xAxis': { 'type': 'category' },
        'yAxis': { 'gridIndex': 0 },
        'grid': { 'top': '55%' },
        'series': [
            
            {
            'type': 'line',
            'smooth': True,
            'seriesLayoutBy': 'row',
            'emphasis': { 'focus': 'series' }
            },
            {
            'type': 'line',
            'smooth': True,
            'seriesLayoutBy': 'row',
            'emphasis': { 'focus': 'series' }
            },
            {
            'type': 'pie',
            'id': 'pie',
            'radius': '30%',
            'center': ['50%', '25%'],
            'emphasis': {
                'focus': 'self'
            },
            'label': {
                'formatter': '{b}: {@2012} ({d}%)'
            },
            'encode': {
                'itemName': 'product',
                'value': '2012',
                'tooltip': '2012'
            }
            }
        ]
    }

    return JsonResponse(chart)

def mapStore(request):
    data= [
            [0, 120, 20], [1, 200, 150], [2, 150, 100],[3, 120, 20],
            [1, 200, 150],[3, 150, 100],[8, 120, 20],[4, 200, 150], 
            [5, 150, 100],[6, 120, 20],[7, 200, 150], [4, 150, 100],
            [2, 120, 20],[4, 200, 150],[5, 150, 100],[6, 120, 20],
            [7, 200, 150],[8, 150, 100],[9, 120, 20],[10, 200, 150], 
            [4, 150, 100] 
    ]
    symbol_sizes = [
        math.sqrt(dat[1] + dat[2]) for dat in data
    ]
    option = {
        'title': {
            'text': 'Demanda de Compras y Ventas por Ciudad y Tienda/Evento'
        },
        'xAxis': {
            'type': 'category',
            'data': ['Ciudad A', 'Ciudad B', 'Ciudad C', 'Ciudad D', 'Ciudad E', 'Ciudad F', 'Ciudad G', 'Ciudad H', 'Ciudad I', 'Ciudad J', 'Ciudad K']
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
                'type': 'scatter',
                'data': data,
                'symbolSize': symbol_sizes,
                'emphasis': {
                    'focus': 'series'
                }
            }
        ]
    }
    return JsonResponse(option)

def barDemand(request):
    events = [
        {"name": "Evento 1", "date": "2023-08-01", "before_demand": 50, "during_demand": 80, "after_demand": 60},
        {"name": "Evento 2", "date": "2023-08-10", "before_demand": 70, "during_demand": 120, "after_demand": 90},
        {"name": "Evento 3", "date": "2023-08-20", "before_demand": 60, "during_demand": 100, "after_demand": 75},
        # ... Agrega más eventos si es necesario
    ]
    beforeDemand = [event["before_demand"] for event in events]
    duringDemand = [event["during_demand"] for event in events]
    afterDemand = [event["after_demand"] for event in events]
    categories = [event["name"] for event in events]
    
    # Crea el JsonResponse
    chart = {
        'legend': {
                'data': ['Antes', 'Durante', 'Después']
            },
            'xAxis': {
                'data': categories
            },
            'yAxis': {},
            'series': [
                {
                    'name': 'Antes',
                    'type': 'bar',
                    'data': beforeDemand
                },
                {
                    'name': 'Durante',
                    'type': 'bar',
                    'data': duringDemand
                },
                {
                    'name': 'Después',
                    'type': 'bar',
                    'data': afterDemand
                }
            ]
    }

    return JsonResponse(chart)

