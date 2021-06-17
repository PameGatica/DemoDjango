from django.urls import path
from .views import index
from .views import contacto
from .views import listarVehiculos
from .views import nuevoVehiculo

urlpatterns = [
    path('',index,name="index"),
    path('contacto/',contacto,name="contacto"),
    path('vehiculo/listar',listarVehiculos, name="listarVehiculos"),
    path('vehiculo/agregar',nuevoVehiculo,name="nuevoVehiculo")
]