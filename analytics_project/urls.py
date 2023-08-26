"""
URL configuration for analytics_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from store_analytics_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.home_view, name='home'),
    path('sales_and_purchase_demand/', views.sales_and_purchase_demand_view, name='sales_and_purchase_demand'),
    path('external_events/', views.external_events_view, name='external_events'),
    path('retention_rate/', views.retention_rate_view, name='retention_rate'),
    path('outlier_summary/', views.outlier_summary_view, name='outlier_summary'),
    path('kpi/', views.kpi_view, name='kpi'),
    path('get_chart/', views.get_chart, name='get_chart'),
    path('demand_trends_chart/', views.demand_trends_chart, name='demand_trends_chart'),
    path('mapStore/', views.mapStore, name='mapStore'),
    path('chartBarDemand/', views.barDemand, name='chartBarDemand'),
]
