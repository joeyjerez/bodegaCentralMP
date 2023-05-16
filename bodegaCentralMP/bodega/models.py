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