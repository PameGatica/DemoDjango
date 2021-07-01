from django.urls import path
from .views import detalle_vehiculo, procesar_vehiculos

urlpatterns = [
    path('vehiculos',procesar_vehiculos, name="procesar_vehiculos"),
    path('vehiculos/<id>',detalle_vehiculo, name="detalle_vehiculo")
]
