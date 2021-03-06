# Generated by Django 2.2.13 on 2021-11-08 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211106_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='nombre')),
                ('estatus', models.BooleanField(default=True, verbose_name='Estatus')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Lugar de atención',
                'verbose_name_plural': 'Lugares de atención',
            },
        ),
        migrations.AddField(
            model_name='solicitud',
            name='detalles',
            field=models.TextField(null=True, verbose_name='Detalles'),
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga', models.BooleanField(default=True, verbose_name='Carga de solicitudes')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('zona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Zona')),
            ],
            options={
                'verbose_name': 'Población Objetivo',
                'verbose_name_plural': 'Poblaciones objetivo',
            },
        ),
        migrations.AddField(
            model_name='solicitud',
            name='zona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Zona'),
        ),
    ]
