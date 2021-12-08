# Generated by Django 2.2.13 on 2021-11-27 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_auto_20211126_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroImpresion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('solcitud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Solicitud')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Configuración',
                'verbose_name_plural': 'Configuraciones',
            },
        ),
    ]