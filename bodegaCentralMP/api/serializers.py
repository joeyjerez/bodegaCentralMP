from rest_framework import serializers
from bodega.models import *

class ProductoSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo','nombre']

class DetallePedidoSerializer(serializers.ModelSerializer):
    producto_codigo = serializers.ReadOnlyField(source='producto.codigo')
    class Meta:
        model = DetallePedido
        fields = ['producto_codigo','cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    productos = DetallePedidoSerializer(source='detallepedido_set', many=True)
    class Meta:
        model = Pedido
        fields = [
            'id_pedido',
            'fecha_pedido',
            'sucursal',
            'productos',
            'estado',
            'total',
        ]