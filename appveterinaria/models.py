from django.db import models

# Create your models here.


class Alimentogato(models.Model):
    marca = models.CharField(max_length=150)
    precio = models.IntegerField (default=0)
    info = models.CharField(max_length=150, default=0)
    
    def __str__(self):
        return f"{self.precio} - {self.marca} - {self.info}"

class Alimentoperro(models.Model):
    marca = models.CharField(max_length=150)
    precio = models.IntegerField (default=0)
    info= models.CharField(max_length=150, default=0)
    
    def __str__(self):
        return f"{self.precio} - {self.marca} - {self.info}"

class Alimentopeces(models.Model):
    marca = models.CharField(max_length=150)
    precio = models.IntegerField (default=0)
    info = models.CharField(max_length=150, default=0)
    
    def __str__(self):
        return f"{self.precio} - {self.marca} - {self.info}"
