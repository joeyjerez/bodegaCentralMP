#from django.shortcuts import render

# Create your views here.
import requests
from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def root(request):
    return redirect('/bodega')

@login_required
def index(request):
    return render(request, 'core/home.html')


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

@login_required
def index(request):
    if request.user.is_authenticated:
        return render(request, 'core/home.html')
    else:
        return redirect('login')

def error404(request):
    return render(request, 'core/404.html')

@login_required
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

@login_required
def productos_list(request):
    context = {'productos' : Producto.objects.all()}
    return render(request, 'core/producto/productos.html', context)

@login_required
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

@login_required
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

@login_required
def productos_delete(request, codigo):
    try:
        producto = Producto.objects.get(codigo=codigo)
        producto.delete()
        return redirect(to= 'productos_list')
    except:
        return redirect(reverse('productos_list') + "?FAIL")

@login_required
def sucursal_list(request):
    context = {'sucursales' : Sucursal.objects.all()}
    return render(request, 'core/sucursal/sucursales.html', context)

@login_required
def sucursal_new(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            id_sucursal = form.cleaned_data.get("id_sucursal")
            nombre = form.cleaned_data.get("nombre")
            direccion = form.cleaned_data.get("direccion")
            obj = Sucursal.objects.create(
                id_sucursal = id_sucursal,
                nombre = nombre,
                direccion = direccion
            )
            obj.save()
            return redirect(reverse('sucursal_list') + "?OK")
        else:
            return redirect(reverse('sucursal_list') + "?FAIL")
    else:
        form = SucursalForm
    return render(request,'core/sucursal/sucursal_new.html',{'form':form})

@login_required
def sucursal_edit(request, id_sucursal):
    try:
        sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
        if sucursal:
            form = SucursalForm(instance = sucursal)
        else:
            return redirect(reverse('sucursales_list') + "?FAIL")
    
        if request.method == 'POST':
            form = ProductoForm(request.POST or None, instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('sucursales_list') + "?OK")
            else:
                return redirect(reverse('sucursales_edit') + id_sucursal)
        return render(request,'core/sucursal/sucursal_edit.html',{'form':form})   
    except:
        return redirect(reverse('sucursales_list') + "?FAIL")

@login_required
def sucursal_delete(request, id_sucursal):
    try:
        sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
        sucursal.delete()
        return redirect(to= 'sucursales_list')
    except:
        return redirect(reverse('sucursales_list') + "?FAIL")

@login_required
def pedidos_list(request):
    context = {'pedidos' : Pedido.objects.all()}
    return render(request, 'core/pedido/pedidos.html', context)

@login_required
def pedidos_new(request):
    if request.method == 'POST':

        id_pedido = request.POST.get('pedido')
        # print(id_pedido)
        sucursal_id = request.POST.get('sucursal')
        # print(sucursal_id)
        productos = request.POST.getlist('productos[]')
        # print(productos)
        estado = request.POST.get('estado')
        # print(estado)
        total = request.POST.get('total-pedido')
        # print(total)
        
        sucursal = Sucursal.objects.get(id_sucursal=sucursal_id)
        pedido = Pedido.objects.create(id_pedido=id_pedido, sucursal=sucursal, estado=estado, total=total)
        pedido.save()

        for producto_id in productos:
            producto = Producto.objects.get(codigo=producto_id)
            cantidad = int(request.POST.get('cantidad-' + producto_id))
            subtotal = producto.precio * cantidad
            pedidoProducto = DetallePedido.objects.create(pedido=pedido, producto=producto, cantidad=cantidad, subtotal=subtotal)
            pedidoProducto.save()
        return redirect(reverse(pedidos_list) + "?OK")
    else:

        productos = Producto.objects.all()
        sucursales = Sucursal.objects.all()
        context = {
            'productos': productos,
            'sucursales': sucursales,
        }
    return render(request, 'core/pedido/pedido_new.html', context)

@login_required
def pedidos_detalle(request, id_pedido):
    try:
        pedido = Pedido.objects.get(id_pedido = id_pedido)
        detalle = DetallePedido.objects.filter(pedido_id = id_pedido)
        productos = Producto.objects.all()
        print(detalle)
        return render(request, 'core/pedido/pedido_detalle.html',
        {
            'pedido':pedido,
            'detalle':detalle,
            'productos':productos,
        })
    except:
        return render(redirect(pedidos_list))

@login_required
def pedidos_edit(request, id_pedido):
    try:
        pedido = Pedido.objects.get(id_pedido=id_pedido)
        if producto:
            form = PedidoForm(instance = pedido)
        else:
            return redirect(reverse('pedidos_list') + "?FAIL")
    
        if request.method == 'POST':
            form = PedidoForm(request.POST or None, instance=pedido)
            if form.is_valid():
                form.save()
                return redirect(reverse('pedidos_list') + "?OK")
            else:
                return redirect(reverse('pedidos_edit') + id_pedido)
        return render(request,'core/pedido/pedido_edit.html',{'form':form})   
    except:
        return redirect(reverse('pedidos_list') + "?FAIL")

@login_required
def pedidos_delete(request, id_pedido):
    try:
        pedido = Pedido.objects.get(id_pedido=id_pedido)
        pedido.delete()
        return redirect(to= 'pedidos_list')
    except:
        return redirect(reverse('pedidos_list') + "?FAIL")

#Agregar sólo código dentro del método a la vista "pedidos_new"?????
# def carrito(request, id_pedido):
#     carrito = Carrito.objects.filter(pedido = id_pedido)
#     contador = Carrito.objects.count()

#     datos = {
#         'pedido': id_pedido,
#         'productos': carrito,
#         'cantidad': contador,
#         'total': 0,
#         'contar': 0,
#     }
    
#     for producto in carrito:
#         datos['subtotal'] = round(carrito.producto.precio * carrito.producto.cantidad)
#         datos['total'] += round(carrito.producto.precio * carrito.producto.cantidad)

#     if request.method == 'POST':
#         for i in carrito:
#             pedido = Pedido.objects.create()

#             pedido.id_pedido

def admin_view(request):
    return redirect('admin/')
