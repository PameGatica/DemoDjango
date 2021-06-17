from typing import ValuesView
from core.forms import VehiculoForm
from django.shortcuts import redirect, render
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


def modificarVehiculo(request,id):

    vehiculo = Vehiculo.objects.get(patente=id)

    datos={
        'form' : VehiculoForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST,instance=vehiculo)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Datos modificados exitosamente"

    return render(request,'core/formModVehiculo.html',datos)

def eliminarVehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()

    return redirect(to="verVehiculos")