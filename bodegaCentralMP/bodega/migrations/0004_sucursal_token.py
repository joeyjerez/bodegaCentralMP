# Generated by Django 4.2.1 on 2023-06-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0003_alter_pedido_fecha_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='token',
            field=models.CharField(default='secret', max_length=12, unique=True, verbose_name='Token'),
        ),
    ]