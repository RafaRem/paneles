# Generated by Django 2.2.13 on 2021-11-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_serviciossolicitud_seguimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='correo',
            field=models.CharField(blank=True, max_length=200, verbose_name='correo'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='detalles',
            field=models.TextField(blank=True, null=True, verbose_name='Detalles'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='telefono',
            field=models.CharField(blank=True, max_length=200, verbose_name='teléfono'),
        ),
    ]
