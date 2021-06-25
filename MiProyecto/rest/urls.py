from django.urls import path
from .views import lista_vehiculos


urlpatterns = [
    path('vehiculo/listar', lista_vehiculos, name='lista_vehiculos'),
]
