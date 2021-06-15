from django.urls import path
from .views import index
from .views import contacto
from .views import verVehiculos
from .views import nuevoVehiculo

urlpatterns = [
    path('',index, name='index'),
    path('contacto/',contacto, name='contacto'),
    path('vehiculo/listar',verVehiculos, name='verVehiculos'),
    path('vehiculo/nuevo',nuevoVehiculo,name="nuevoVehiculo")
]