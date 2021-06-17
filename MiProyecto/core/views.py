from django.shortcuts import render
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