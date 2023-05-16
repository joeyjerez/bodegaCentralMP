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