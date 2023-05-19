from django import forms
from django.forms import ModelForm
from .models import *

# Ingresar aquí las clases de la base de datos

# Ejemplo:
#
# class MiembroForm(ModelForm):
#     class Meta:
#         model = Miembro
#         fields = [
#             'idMiembro',
#             'nombre',
#             'apellidos',
#             'ocupacion',
#             'correo',
#             'foto'
#         ]
#         labels = {
#             'idMiembro': 'ID Miembro',
#             'nombre': 'Nombre',
#             'apellidos': 'Apellidos',
#             'ocupacion': 'Ocupación',
#             'correo': 'Correo',
#             'foto': 'Foto'
#         }
#         widgets = {
#             'idMiembro': forms.TextInput(attrs={'class':'form-control','type':'number'}),
#             'nombre': forms.TextInput(attrs={'class':'form-control'}),
#             'apellidos': forms.TextInput(attrs={'class':'form-control'}),
#             'ocupacion': forms.TextInput(attrs={'class':'form-control'}),
#             'correo': forms.TextInput(attrs={'class':'form-control'}),
#             'foto': forms.FileInput(attrs={'class':'form-control'})
#         }

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        
        fields = [
            'nombre',
            'apellido',
            'cargo',
            'correo',
            'contraseña',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cargo': 'Cargo',
            'correo': 'Correo',
            'contraseña': 'Contraseña',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'cargo': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'contraseña': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        
        fields = [
            'codigo',
            'nombre',            
            'descripcion',            
            'marca',
            'imagen',
            'precio',
        ]
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'marca': 'Marca',
            'imagen': 'Imagen',
            'precio': 'Precio',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'required': True, 'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'size': 50, 'required': True, 'title': 'Nombre del producto', 'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'size': 320, 'required': False, 'title': 'Descripción del producto', 'class':'form-control'}),
            'marca': forms.TextInput(attrs={'size': 80, 'required': True, 'title': 'Marca del fabricante', 'class':'form-control'}),
            'imagen': forms.FileInput(attrs={'required': True, 'class':'form-control'}),
            'precio': forms.TextInput(attrs={'required': False, 'type':'number', 'class':'form-control'})
        }