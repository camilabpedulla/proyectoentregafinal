from django.db import models

# Create your models here.


class Alimentogato(models.Model):
    marca = models.CharField(max_length=150)
    precio = models.FloatField()
    fecha_vencimiento= models.DateField(blank=True, null=True)
    stock = models.IntegerField()

class Alimentoperro(models.Model):
    marca = models.CharField(max_length=150)
    precio = models.FloatField()
    fecha_vencimiento= models.DateField(blank=True, null=True)
    stock = models.IntegerField()

class Alimentopeces(models.Model):
    marca = models.CharField(max_length=150)
    precio = models.FloatField()
    fecha_vencimiento= models.DateField(blank=True, null=True)
    stock = models.IntegerField()
    def __str__(self):
        return f"{self.precio} - {self.marca}"
