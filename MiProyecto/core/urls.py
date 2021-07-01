from django.urls import path
from core.views import index, contacto, listarVehiculos, agregarVehiculo, editarVehiculo,eliminarVehiculo

urlpatterns = [
    path('',index, name="index"),
    path('contacto/',contacto, name="contacto"),
    path('vehiculo/listar',listarVehiculos, name="listarVehiculos"),
    path('vehiculo/agregar',agregarVehiculo,name="agregarVehiculo"),
    path('vehiculo/editar/<id>',editarVehiculo,name="editarVehiculo"),
    path('vehiculo/eliminar/<id>',eliminarVehiculo,name="eliminarVehiculo")

]