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

