from django.shortcuts import redirect, render
from .models import Categoria
from .models import Vehiculo
from .forms import VehiculoForm
from .functions import validaVehiculo

def index(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request,'core/contacto.html')

def categorias(request):
    cate = Categoria.objects.all()

    datos = {
        'categorias' : cate
    }
    return render(request,'core/categorias.html', datos)

def vehiculos(request):
    ve = Vehiculo.objects.all()

    datos = {
        'vehiculos' : ve
    }
    return render(request,'core/vehiculos.html', datos)

def form_vehiculo(request):
    datos = {
       'form' : VehiculoForm()
    }

    if request.method == 'POST':

        form = VehiculoForm(request.POST)
        patente = request.POST.get("patente")

        if form.is_valid:
            if not validaVehiculo(patente):
                form.save()
                datos['mensaje'] = "Vehículo guardado exitosamente"
            else:
                 datos['mensaje'] = "Ya existe un registro asociado a la patente " + patente

    return render(request,'core/nuevoVehiculo.html',datos)

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