from django.db import models

class Producto(models.Model):

    # nuevo = "Nuevo"
    # usado = "Usado"
    # reaco = "Reacondicionado"

    # LISTA_ESTADOS = [
    #     (nuevo, "Nuevo"),
    #     (usado, "Usado"),
    #     (reaco, "Reacondicionado")
    # ]

    codigo = models.IntegerField(verbose_name='Codigo', null=False)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', null=False)
    # estado = models.CharField(max_length=5, choices=LISTA_ESTADOS, default=nuevo)
    stock = models.IntegerField(verbose_name='Stock', null=False, default=0)
    descripcion = models.CharField(max_length=400, verbose_name='Descripción')
    marca = models.CharField(max_length=80, verbose_name='Marca')
    precio = models.IntegerField(verbose_name='Precio', null=False, default=0)
    imagen = models.ImageField(null=True, blank=True, verbose_name='Imagen', upload_to='productos/')
    # pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering=['codigo']

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(verbose_name='ID Sucursal', null=False)
    nombre = models.CharField(verbose_name='Nombre de Sucursal', null=False, max_length=150)
    dirección = models.CharField(verbose_name='Dirección', null=False, max_length=120)

    class Meta:
        verbose_name='sucursal'
        verbose_name_plural='sucursales'
        ordering=['id_sucursal']

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    id_pedido = models.IntegerField(verbose_name='ID Pedido', null=False)
    fecha_pedido = models.DateField(verbose_name='Fecha del Pedido', auto_now_add=True)
    sucursal= models.ForeignKey(Sucursal, on_delete= models.CASCADE, null=False)

    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id_pedido']
    
    def __str__(self):
        return self.id_pedido