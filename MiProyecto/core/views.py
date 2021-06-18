from django.forms.widgets import DateTimeBaseInput
from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request,'core/contacto.html')

def listarVehiculos(request):
    vehiculos = Vehiculo.objects.all()

    datos = {
        'vehiculos' : vehiculos
    }

    return render(request,'core/listarVehiculos.html',datos)

def nuevoVehiculo(request):
    form = VehiculoForm()

    datos = {
        'form' : form
    }

    if request.method == 'POST' :
        form = VehiculoForm(request.POST)
        if form.is_valid:
            form.save()
            datos['mensaje'] = 'Vehículo creado exitosamente'


    return render(request,'core/nuevoVehiculo.html', datos)

def editarVehiculo(request,id):

    vehiculo = Vehiculo.objects.get(patente=id)

    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Datos modificados correctamente'

    return render(request,'core/editarVehiculo.html', datos)

def eliminarVehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to="listarVehiculos")

