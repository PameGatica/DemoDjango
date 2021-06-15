from core.forms import VehiculoForm
from django.shortcuts import render
from .models import Vehiculo

def index(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request,'core/contacto.html')

def verVehiculos(request):
    vehiculos = Vehiculo.objects.all()

    datos ={
        'vehiculos' : vehiculos
    }

    return render(request, 'core/listarVehiculos.html',datos)

def nuevoVehiculo(request):

    datos = {
        'form': VehiculoForm()
    }

    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Datos guardados exitosamente'
        else:
            datos['mensaje'] = 'Error'
    return render(request, 'core/formVehiculo.html',datos)