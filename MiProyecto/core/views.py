from django import forms
from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def listarVehiculos(request):
    vehiculos = Vehiculo.objects.all()

    datos = {
        'vehiculos' : vehiculos
    }
    return render(request,'core/listarVehiculos.html',datos)


def agregarVehiculo(request):

   # form = VehiculoForm()

    datos = {
        'form' : VehiculoForm()
    }

    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Vehiculo agregado exitosamente'


    return render (request,'core/agregarVehiculo.html',datos)

def editarVehiculo(request,patente):

    vehiculo = Vehiculo.objects.get(patente=patente)

    datos = {
    'form' : VehiculoForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST,instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Vehículo modificado exitosamente"


    return render(request,'core/editarVehiculo.html',datos)


def eliminarVehiculo(request,patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.delete()

    return redirect(to="vehiculos")    