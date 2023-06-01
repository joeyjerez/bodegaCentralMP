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