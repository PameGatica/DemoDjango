from django.urls import path
from .views import index
from .views import contacto
from .views import listarVehiculos
from .views import nuevoVehiculo
from .views import editarVehiculo
from .views import eliminarVehiculo

urlpatterns = [
    path('',index,name="index"),
    path('contacto/',contacto,name="contacto"),
    path('vehiculo/listar',listarVehiculos, name="listarVehiculos"),
    path('vehiculo/agregar',nuevoVehiculo,name="nuevoVehiculo"),
    path('vehiculo/editar/<id>',editarVehiculo,name="editarVehiculo"),
    path('vehiculo/eliminar/<id>',eliminarVehiculo,name="eliminarVehiculo")
]