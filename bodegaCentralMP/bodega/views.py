#from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

def root(request):
    return redirect('/bodega')

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def saludo(request):
    
    url = "https://musicpro.bemtorres.win/api/v1/test/saludo"

    try:
        response = request.get(url)
        data = response.json()

        print(data['message'])

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    
    return HttpResponse("¡Saludo completado!")