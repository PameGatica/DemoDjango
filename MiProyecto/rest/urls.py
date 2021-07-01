from django.urls import path
from .views import detalle_vehiculo, lista_vehiculos


urlpatterns = [
    path('vehiculo/listar', lista_vehiculos, name='lista_vehiculos'),
    path('vehiculo/detalle/<id>', detalle_vehiculo, name="detalle_vehiculo"),
]
