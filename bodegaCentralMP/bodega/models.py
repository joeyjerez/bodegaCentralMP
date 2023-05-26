from django.db import models

# Create your models here.
#run-nombre-apellido-correo-contraseña
class Usuario(models.Model):
    run=models.CharField(max_length=15)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
