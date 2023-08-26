from django.db import models

class Store(models.Model):
    pdv = models.IntegerField(primary_key=True)
    idregion = models.IntegerField()
    idciudad = models.IntegerField()
    canal = models.CharField(max_length=50)
    actividad = models.CharField(max_length=50)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)

class ExternalEvent(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateField()
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)

class PurchaseData(models.Model):
    pdv = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class SalesData(models.Model):
    pdv = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class RetentionData(models.Model):
    pdv = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField()
    retention_rate = models.DecimalField(max_digits=5, decimal_places=2)
