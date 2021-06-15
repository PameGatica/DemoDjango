from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoría')
    nombreCategoria = models.CharField(max_length=60,verbose_name="Categoría")

    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente