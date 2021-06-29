from .serializers import VehiculoSerializer
from django.shortcuts import render
from core.models import Vehiculo
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
@api_view(['GET','POST'])

def procesar_vehiculos(request):
    if request.method == 'GET' :  #LISTAR TODOS LOS VEHICULOS
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':  #AGREGAR UN NUEVO VEHÍCULO
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)