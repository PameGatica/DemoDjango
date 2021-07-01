from .models import Vehiculo


def validaVehiculo(patente):
    existe = Vehiculo.objects.filter(patente=patente).exists()
    return existe
