from django.urls import path
from django.conf.urls import  url
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contacto/',views.contacto, name='contacto'),
    path('categorias/',views.categorias, name='categorias'),
    path('vehiculos/',views.vehiculos, name='vehiculos'),
    path('vehiculos/nuevo',views.form_vehiculo, name='nuevo-vehiculo'),
    path('vehiculos/editar/<patente>', views.editarVehiculo, name='editarVehiculo'),
    path('vehiculos/eliminar/<patente>',views.eliminarVehiculo, name='eliminarVehiculo')
    
    
]