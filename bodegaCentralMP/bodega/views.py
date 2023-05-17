#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

def root(request):
    return redirect('/bodega')

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')