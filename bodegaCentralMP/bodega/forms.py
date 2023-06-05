from django import forms
from django.forms import ModelForm
from .models import *

# Ingresar aquí las clases de la base de datos

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        
        fields = '__all__'
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
            # 'estado': 'Estado',
            'stock': 'Stock',
            'descripcion': 'Descripción',
            'marca': 'Marca',
            'precio': 'Precio',
            'imagen': 'Imagen',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'required': True, 'type':'number','title':'Código de producto', 'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'size': 50, 'required': True, 'title': 'Nombre del producto', 'class':'form-control'}),
            'stock': forms.TextInput(attrs={'required': True, 'title': 'Stock', 'type':'number', 'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'size': 320, 'required': False, 'title': 'Descripción del producto', 'default':'Sin descripción', 'class':'form-control'}),
            'marca': forms.TextInput(attrs={'size': 80, 'required': True, 'title': 'Marca del fabricante', 'class':'form-control'}),
            'precio': forms.TextInput(attrs={'required': False, 'type':'number','title':'Precio', 'class':'form-control pesos'})
        }

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal

        fields = '__all__'
        labels = {
            'id_sucursal' : 'ID Sucursal',
            'nombre' : 'Nombre de Sucursal',
            'direccion' : 'Dirección'
        }
        widgets = {
            'id_sucursal': forms.TextInput(attrs={'required':True,'type':'number','title':'ID Sucursal','class':'form-control'}),
            'nombre': forms.TextInput(attrs={'required':True,'title':'Nombre de Sucursal','class':'form-control'}),
            'direccion': forms.TextInput(attrs={'required':True,'title':'Dirección','class':'form-control'}),
        }

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido

        fields = "__all__"
        labels = ""
        widgets = {
            'id_pedido': forms.TextInput(attrs={'required':True,'type':'number','title':'ID Pedido','class':'form-control'}),
            'sucursal': forms.Select(attrs={'required':True,'title':'Sucursal','class':'form-control'}),
            'productos': forms.Select(attrs={'required':True,'title':'Productos','class':'form-control align-top','id':'productos','name':'productos'}),
            'estado': forms.Select(attrs={'title':'Estado','class':'form-select'})
            # 'cantidad': forms.TextInput(attrs={'required':True,'type':'number','title':'Cantidad','class':'form-control'}),
        }

# class PedidoForm(forms.Form):
#     id_pedido = forms.IntegerField(min_value=1)
#     sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all())
#     productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all())
#     cantidad = forms.IntegerField(min_value=1)

#     def clean_cantidad(self):
#         cantidad = self.cleaned_data.get('cantidad')
#         if len(cantidad) != len(self.cleaned_data.get('productos')):
#             raise forms.ValidationError("Debe especificar una cantidad para cada producto.")
#         return cantidad

#     class Meta:
#         fields = "__all__"
#         labels = {
#             'id_pedido' : 'ID Pedido',
#             'sucursal' : 'Sucursal',
#             'cantidad' : 'cantidad'
#         }
#         widgets = {
#             'id_pedido': forms.TextInput(attrs={'required':True,'type':'number','title':'ID Pedido','class':'form-control'}),
#             'sucursal': forms.TextInput(attrs={'required':True,'title':'Sucursal','class':'form-control'}),
#             'cantidad': forms.TextInput(attrs={'required':True,'type':'number','title':'Cantidad','class':'form-control'}),
#         }