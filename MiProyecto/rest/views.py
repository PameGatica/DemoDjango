from .serializers import VehiculoSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from core.models import Vehiculo


@csrf_exempt
@api_view(['GET','POST'])

#Si request es por GET: accedimos a una URL para listar los elementos
#Si el request es por POST: enviando elementos a la vista (Por ejemplo desde un formulario)
def lista_vehiculos(request):
    if request.method == 'GET':
        #Listo los vehiculos desde la BD
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


#Si request es por GET: accedimos a una URL para ver el detalle de un vehículo
#Si request es por PUT: modificamos los datos del vehículo cuya patente se envío por la URL
#Si request es por DELETE: eliminamos el vehículo cuya patente se envío por la URL
@api_view(['GET','PUT','DELETE'])
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
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        vehiculo.delete()
        return Response(status.HTTP_204_NO_CONTENT)
