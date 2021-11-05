from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Direccion(models.Model):
    nombre = models.CharField(  max_length=200, verbose_name="nombre")
    estatus = models.BooleanField(verbose_name=("Estatus"), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Dirección"

    def __str__(self):
        return self.nombre

class ServiciosSolicitud(models.Model):
    nombre = models.CharField(  max_length=200, verbose_name="nombre")
    direccion = models.ForeignKey(Direccion, on_delete=models.PROTECT)
    estatus = models.BooleanField(verbose_name=("Estatus"), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    nombre = models.CharField(  max_length=50, verbose_name="nombre")
    appaterno = models.CharField(  max_length=30, verbose_name="apellido paterno")
    apmaterno = models.CharField(  max_length=30, verbose_name="apellido materno")
    curp = models.CharField(  max_length=50, verbose_name="CURP")
    estcivil = models.CharField(  max_length=50, verbose_name="estcivil")
    discapacidad = models.CharField(  max_length=50, verbose_name="discapacidad")
    domicilio = models.CharField(  max_length=50, verbose_name="domicilio")
    correo = models.CharField(  max_length=50, verbose_name="correo")
    telefono = models.CharField(  max_length=50, verbose_name="teléfono")
    sexo = models.CharField(  max_length=50, verbose_name="sexo", null=True)
    servicios = models.ManyToManyField(ServiciosSolicitud, blank=True)
    estatus = models.BooleanField(verbose_name=("Estatus"), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitud"

    def __str__(self):
        return self.nombre