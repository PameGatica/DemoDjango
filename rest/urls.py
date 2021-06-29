from django.urls import path
from .views import procesar_vehiculos

urlpatterns = [
    path('vehiculos',procesar_vehiculos, name="procesar_vehiculos")
]
