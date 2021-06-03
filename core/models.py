from django.db import models
from django.db.models.base import Model

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True,max_length=6,verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca Vehículo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
