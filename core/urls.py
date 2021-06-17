from django.urls import path
from .views import index
from .views import contacto
from .views import verVehiculos
from .views import nuevoVehiculo
from .views import modificarVehiculo
from .views import eliminarVehiculo

urlpatterns = [
    path('',index, name='index'),
    path('contacto/',contacto, name='contacto'),
    path('vehiculo/listar',verVehiculos, name='verVehiculos'),
    path('vehiculo/nuevo',nuevoVehiculo,name='nuevoVehiculo'),
    path('vehiculo/editar/<id>', modificarVehiculo, name='modificarVehiculo'),
    path('vehiculo/eliminar/<id>',eliminarVehiculo, name='eliminarVehiculo')
]