# Generated by Django 2.2.25 on 2022-02-02 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adicional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(max_length=200, verbose_name='Folio')),
                ('solicitud', models.CharField(max_length=200, verbose_name='Id Solicitud')),
                ('name_attended', models.CharField(max_length=200, verbose_name='Nombre')),
                ('total_people', models.CharField(max_length=200, verbose_name='Habitantes')),
                ('disability', models.CharField(max_length=200, verbose_name='personas con discapacidad')),
                ('mom', models.CharField(max_length=200, verbose_name='madres solteras')),
                ('adult', models.CharField(max_length=200, verbose_name='adultos mayores')),
                ('younger', models.CharField(max_length=200, verbose_name='menores de edad')),
                ('house', models.CharField(max_length=200, verbose_name='Casa')),
                ('ceiling', models.CharField(max_length=200, verbose_name='Techo')),
                ('floor', models.CharField(max_length=200, verbose_name='Piso')),
                ('bath', models.CharField(max_length=200, verbose_name='Baño')),
                ('estatus', models.BooleanField(default=True, verbose_name='Estatus')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Información Bienestar',
                'verbose_name_plural': 'Información Bienestar',
            },
        ),
    ]
