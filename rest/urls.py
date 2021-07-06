from django.urls import path
from .views import detalle_vehiculo, procesar_vehiculos
from .viewslogin import login

urlpatterns = [
    path('vehiculos',procesar_vehiculos, name="procesar_vehiculos"),
    path('vehiculos/<id>',detalle_vehiculo, name="detalle_vehiculo"),
    path('login',login,name="login")
]
