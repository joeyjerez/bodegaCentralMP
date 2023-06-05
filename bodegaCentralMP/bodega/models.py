from django.db import models

class Producto(models.Model):

    # nuevo = "Nuevo"
    # usado = "Usado"
    # reaco = "Reacondicionado"

    # LISTA_CONDICION = [
    #     (nuevo, "Nuevo"),
    #     (usado, "Usado"),
    #     (reaco, "Reacondicionado")
    # ]

    codigo = models.IntegerField(verbose_name='Codigo', null=False, unique=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', null=False)
    # estado = models.CharField(max_length=5, choices=LISTA_CONDICION, default=nuevo)
    stock = models.IntegerField(verbose_name='Stock', null=False, default=0)
    descripcion = models.CharField(max_length=400, verbose_name='Descripción')
    marca = models.CharField(max_length=80, verbose_name='Marca')
    precio = models.IntegerField(verbose_name='Precio', null=False, default=0)
    imagen = models.ImageField(null=True, blank=True, verbose_name='Imagen', upload_to='productos/')

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering=['codigo']

    def __str__(self):
        return self.nombre + " - ${:0,.0f}".format(self.precio)

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(verbose_name='ID Sucursal', unique=True)
    nombre = models.CharField(verbose_name='Nombre de Sucursal', null=False, max_length=150)
    direccion = models.CharField(verbose_name='Dirección', null=False, max_length=120)

    class Meta:
        verbose_name='sucursal'
        verbose_name_plural='sucursales'
        ordering=['id_sucursal']

    def __str__(self):
        return self.nombre

class Pedido(models.Model):

    pend = "Pendiente"
    envi = "Enviado"
    compl = "Completado"

    LISTA_ESTADOS = [
        (pend, 'Pendiente'),
        (envi, 'Enviado'),
        (compl, 'Completado')
    ]

    id_pedido = models.CharField(max_length=9, unique=True, verbose_name='ID Pedido', null=False)
    fecha_pedido = models.DateField(verbose_name='Fecha del Pedido', auto_now_add=True)
    sucursal= models.ForeignKey(Sucursal, on_delete= models.CASCADE, null=False)
    productos = models.ManyToManyField(Producto, through='ProductoPedido')
    estado= models.CharField(max_length=10, choices=LISTA_ESTADOS, verbose_name='Estado', default=pend, null=False)

    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id_pedido']
    
    def __str__(self):
        return f"Pedido #{self.id_pedido}"

class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1, null=False)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en {self.pedido.__str__()}"