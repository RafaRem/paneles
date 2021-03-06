# Generated by Django 2.2.13 on 2021-11-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20211116_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviciossolicitud',
            name='cantidad',
            field=models.CharField(default='0', max_length=200, verbose_name='cantidad de stock para la feria'),
        ),
        migrations.AddField(
            model_name='serviciossolicitud',
            name='limite',
            field=models.BooleanField(default=False, verbose_name='¿Tiene limite de stock para la feria?'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='calle',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='calle'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='codigo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='código postal'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='exterior',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='exterior'),
        ),
    ]
