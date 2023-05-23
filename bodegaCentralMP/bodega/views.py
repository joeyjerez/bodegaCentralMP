#from django.shortcuts import render

# Create your views here.
import requests

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext 


def index(request):
    return render(request, 'core/home.html')

def productos(request):
    return render(request, 'core/productos.html')

def usuarios(request):
    return render(request, 'core/usuarios.html')





def saludo(request):
    url = "http://musicpro.bemtorres.win/api/v1/test/saludo"

    try:
        response = requests.get(url)
        data = response.json()

        print(data["message"])

    except requests.exceptions.RequestException as e:
        print(f'error; {e}')

    return HttpResponse("solicitud completada") 


