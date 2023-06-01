from django import forms
from django.forms import ModelForm
from .models import *

# Ingresar aquí las clases de la base de datos

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        
        fields = [
            'rut',
            'nombre',
            'apellido',
            'cargo',
            'correo',
            'contrasena',
        ]
        labels = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cargo': 'Cargo',
            'correo': 'Correo',
            'contrasena': 'Contraseña',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'size':'21', 'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'size':'40', 'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'size':'40', 'class':'form-control'}),
            'cargo': forms.TextInput(attrs={'size':'100', 'class':'form-control'}),
            'correo': forms.TextInput(attrs={'size':'320', 'class':'form-control'}),
            'contrasena': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        
        fields = '__all__'
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
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
            'descripcion': forms.TextInput(attrs={'size': 320, 'required': False, 'title': 'Descripción del producto', 'default':'Sin descripción', 'class':'form-control'}),
            'marca': forms.TextInput(attrs={'size': 80, 'required': True, 'title': 'Marca del fabricante', 'class':'form-control'}),
            'precio': forms.TextInput(attrs={'required': False, 'type':'number','title':'Precio', 'class':'form-control'})
        }