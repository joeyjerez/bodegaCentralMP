import requests
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from bodega.models import *
from .serializers import *

# Create your views here.

def root(request):
    return redirect(producto_list)

def saludo(request):
    url = "https://musicpro.bemtorres.win/api/v1/test/saludo"

    try:
        response = requests.get(url)
        data = response.json()

        print(data['message'])

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    
    return HttpResponse("¡Saludo completado!")

@api_view(['GET', 'POST', 'DELETE'])
def producto_list(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        productos_serializer = ProductoSerializer(productos,many=True)
        return Response(productos_serializer.data)

    elif request.method == 'POST':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data, status=status.HTTP_201_CREATED)
        return Response(producto_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cantidad = Producto.objects.all().delete()
        return Response({'mensaje':'¡{} productos han sido eliminados de la base de datos!'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def producto_detail(request, codigo):
    try:
        producto = Producto.objects.get(codigo=codigo)
    except:
        return Response({'mensaje':'El producto con código {} no existe'.format(codigo)},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        producto_serializer = ProductoSerializer(producto)
        return Response(producto_serializer.data)

    elif request.method == 'PUT':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(producto,data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(producto_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        producto.delete()
        return Response({'mensaje':'¡El producto con el código {} ha sido eliminado satisfactoriamente!'.format(codigo)},status=status.HTTP_204_NO_CONTENT)
