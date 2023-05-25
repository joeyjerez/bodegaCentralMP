from django.db import models

# Create your models here.

# Ejemplo
#
# class Miembro(models.Model):
#     idMiembro = models.IntegerField(primary_key=True, verbose_name='ID')
#     nombre = models.CharField(max_length=20, verbose_name='Nombre')
#     apellidos = models.CharField(max_length=30, verbose_name='Apellidos')
#     ocupacion = models.CharField(max_length=100, verbose_name='Ocupación')
#     correo = models.CharField(max_length=50, verbose_name='Correo')
#     foto = models.ImageField(verbose_name='Foto', upload_to='nosotros',null=False)

#     class Meta:
#         verbose_name='miembro'
#         verbose_name_plural='miembros'
#         ordering=['idMiembro']

#     def __str__(self):
#         return self.nombre

class Usuario(models.Model):
    rut = models.CharField(max_length=21, verbose_name='RUT', null=False, default='0-0')
    nombre = models.CharField(max_length=40, verbose_name='Nombre', null=False)
    apellido = models.CharField(max_length=40, verbose_name='Apellido', null=False)
    cargo = models.CharField(max_length=100, verbose_name='Cargo', null=False)
    correo = models.CharField(max_length=320, verbose_name='Correo', null=False)
    contrasena = models.CharField(max_length=256 ,verbose_name='Contraseña', null=False)

    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'
        ordering=['apellido','nombre','rut']

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.IntegerField(verbose_name='Codigo', null=False)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', null=False)
    stock = models.IntegerField(verbose_name='Stock', null=False, default=0)
    descripcion = models.CharField(max_length=400, verbose_name='Descripción')
    marca = models.CharField(max_length=80, verbose_name='Marca')
    imagen = models.ImageField(verbose_name='Imagen', upload_to='productos', default='productos/default.png')
    precio = models.IntegerField(verbose_name='Precio', null=False, default=0)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering=['codigo', 'marca']

    def __str__(self):
        return self.nombre
