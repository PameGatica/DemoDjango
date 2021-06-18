from django.urls import path
from .views import lista_vehiculos

urlpatterns = [
    path('vehiculos/listar', lista_vehiculos,name="lista_vehiculos"),
]
