from re import I
from .serializers import VehiculoSerializer
from django.shortcuts import render
from core.models import Vehiculo
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
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

#GET para listar
#POST para agregar nuevo
#PUT para modificar

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_vehiculo(request, id):
    try:
        vehiculo = Vehiculo.objects.get(patente=id)
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(vehiculo,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'DELETE':
        vehiculo.delete()
        return Response(status.HTTP_204_NO_CONTENT)