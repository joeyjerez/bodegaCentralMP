#from django.shortcuts import render

# Create your views here.
import requests
from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
from .forms import *



def root(request):
<<<<<<< HEAD
    return redirect('/bodega')

def index(request):
    return render(request, 'core/home.html')
=======
    return redirect(index)

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Credenciales inválidas. Inténtalo nuevamente.'
            return render(request, 'core/login.html', {'error_message': error_message})
    return render(request, 'core/login.html')

def index(request):
    if request.user.is_authenticated:
        return render(request, 'core/home.html')
    else:
        return redirect('login')
>>>>>>> c519abf4c9add9c57071298cf6680b107f31b71e

def logout_view(request):
    logout(request)
    return redirect('login')

def saludo(request):
    
    url = "https://musicpro.bemtorres.win/api/v1/test/saludo"

    try:
        response = requests.get(url)
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
        form = ProductoForm(request.POST, request.FILES)
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
            form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
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
        return redirect(reverse('productos_list') + "?FAIL")

<<<<<<< HEAD
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
        return redirect(reverse('usuarios_list') + "?FAIL")
=======
def admin_view(request):
    return redirect('admin/')
>>>>>>> c519abf4c9add9c57071298cf6680b107f31b71e
