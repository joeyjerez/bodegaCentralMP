import requests
from django.shortcuts import render

# Create your views here.

def saludo(request):
    url = "https://musicpro.bemtorres.win/api/v1/test/saludo"

    try:
        response = request.get(url)
        data = response.json()

        print(data['message'])

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    
    return HttpResponse("¡Saludo completado!")

def productos(request):
    pass