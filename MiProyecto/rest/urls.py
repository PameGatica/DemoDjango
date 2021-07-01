from django.urls import path
from rest.views import detalle_vehiculo, lista_vehiculos


urlpatterns = [
    path('vehiculos',lista_vehiculos,name="lista_vehiculos"),
    path('vehiculos/<id>',detalle_vehiculo,name="detalle_vehiculo")
]
