#from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from .forms import *

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

def productos_list(request):
    context = {'productos' : Producto.objects.all()}
    return render(request, 'core/producto/productos.html', context)

def productos_new(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data.get("codigo")
            nombre = form.cleaned_data.get("nombre")
            stock = form.cleaned_data.get("stock")
            marca = form.cleaned_data.get("marca")
            descripcion = form.cleaned_data.get("descripcion")
            imagen = form.cleaned_data.get("imagen")
            precio = form.cleaned_data.get("precio")
            obj = Producto.objects.create(
                codigo = codigo,
                nombre = nombre,
                stock = stock,
                marca = marca,
                descripcion = descripcion,
                imagen = imagen,
                precio = precio,
            )
            obj.save()
            return redirect(reverse('productos_list') + "?OK")
        else:
            return redirect(reverse('productos_list') + "?FAIL")
    else:
        form = ProductoForm
    return render(request,'core/producto/producto_new.html',{'form':form})

def productos_edit(request, codigo):
    try:
        producto = Producto.objects.get(codigo=codigo)
        if producto:
            form = ProductoForm(instance = producto)
        else:
            return redirect(reverse('productos_list') + "?FAIL")
    
        if request.method == 'POST':
            form = ProductoForm(request.POST,request.FILES,instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('productos_list') + "?OK")
            else:
                return redirect(reverse('productos_edit') + codigo)
        return render(request,'core/producto/producto_edit.html',{'form':form})   
    except:
        return redirect(reverse('productos_list') + "?FAIL")

def productos_delete(request, codigo):
    try:
        producto = Producto.objects.get(codigo=codigo)
        producto.delete()
        return redirect(to= 'productos_list')
    except:
        return redirect(reverse('productos_edit') + "?FAIL")

def usuarios_list(request):
    context = {'usuarios' : Usuario.objects.all()}
    return render(request, 'core/usuario/usuarios.html', context)

def usuarios_new(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data.get("rut")
            nombre = form.cleaned_data.get("nombre")
            apellido = form.cleaned_data.get("apellido")
            cargo = form.cleaned_data.get("cargo")
            correo = form.cleaned_data.get("correo")
            contrasena = form.cleaned_data.get("contrasena")
            obj = Usuario.objects.create(
                rut = rut,
                nombre = nombre,
                apellido = apellido,
                cargo = cargo,
                correo = correo,
                contrasena = contrasena,
            )
            obj.save()
            return redirect(reverse('usuarios_list') + "?OK")
        else:
            return redirect(reverse('usuarios_list') + "?FAIL")
    else:
        form = UsuarioForm
    return render(request,'core/usuario/usuario_new.html',{'form':form})

def usuarios_edit(request, rut):
    try:
        usuario = Usuario.objects.get(rut=rut)
        if producto:
            form = UsuarioForm(instance = usuario)
        else:
            return redirect(reverse('usuarios_list') + "?FAIL")
    
        if request.method == 'POST':
            form = UsuarioForm(request.POST,request.FILES,instance=usuario)
            if form.is_valid():
                form.save()
                return redirect(reverse('usuarios_list') + "?OK")
            else:
                return redirect(reverse('usuarios_edit') + rut)
        return render(request,'core/usuario/usuario_edit.html',{'form':form})   
    except:
        return redirect(reverse('usuarios_list') + "?FAIL")

def usuarios_delete(request, rut):
    try:
        usuario = Usuario.objects.get(rut=rut)
        usuario.delete()
        return redirect(to= 'usuarios_list')
    except:
        return redirect(reverse('usuarios_edit') + "?FAIL")
