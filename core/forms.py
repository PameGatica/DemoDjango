from .models import Vehiculo
from django.forms import ModelForm
from django import forms

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']