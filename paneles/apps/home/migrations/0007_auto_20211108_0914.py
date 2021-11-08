# Generated by Django 2.2.13 on 2021-11-08 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211108_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configuracion',
            options={'verbose_name': 'Configuración', 'verbose_name_plural': 'Configuraciones'},
        ),
        migrations.AddField(
            model_name='configuracion',
            name='fecha',
            field=models.DateField(null=True, verbose_name='Fecha proxima atención'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='zona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Zona'),
        ),
    ]
