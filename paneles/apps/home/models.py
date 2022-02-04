from django.db import models

from django.contrib.auth.models import User 
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
    seguimiento = models.BooleanField(verbose_name=("¿Necesita seguimiento?"), default=False)
    limite = models.BooleanField(verbose_name=("¿Tiene limite de stock para la feria?"), default=False, null=True)
    cantidad = models.CharField(  max_length=200, verbose_name="cantidad de stock para la feria", default='0', null=True )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.nombre

class PoblacionObjetivo(models.Model):
    nombre = models.CharField(  max_length=200, verbose_name="nombre")
    estatus = models.BooleanField(verbose_name=("Estatus"), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Población Objetivo"
        verbose_name_plural = "Poblaciones objetivo"

    def __str__(self):
        return self.nombre

class Zona(models.Model):
    nombre = models.CharField(  max_length=200, verbose_name="nombre")
    estatus = models.BooleanField(verbose_name=("Estatus"), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Lugar de atención"
        verbose_name_plural = "Lugares de atención"

    def __str__(self):
        return self.nombre


class Solicitud(models.Model):
    nombre = models.CharField(  max_length=100, verbose_name="nombre")
    appaterno = models.CharField(  max_length=100, verbose_name="apellido paterno")
    apmaterno = models.CharField(  max_length=100, verbose_name="apellido materno")
    curp = models.CharField(  max_length=50, verbose_name="CURP")
    estcivil = models.CharField(  max_length=50, verbose_name="estcivil")
    discapacidad = models.CharField(  max_length=50, verbose_name="discapacidad")
    domicilio = models.CharField(  max_length=100, verbose_name="domicilio")
    calle = models.CharField(  max_length=256, verbose_name="calle", null=True, blank=True)
    exterior = models.CharField(  max_length=50, verbose_name="exterior", null=True, blank=True)
    codigo = models.CharField(  max_length=50, verbose_name="código postal", null=True, blank=True)
    correo = models.CharField(  max_length=200, verbose_name="correo", blank=True)
    telefono = models.CharField(  max_length=200, verbose_name="teléfono", blank=True)
    sexo = models.CharField(  max_length=50, verbose_name="sexo", null=True)
    servicios = models.ManyToManyField(ServiciosSolicitud, blank=True)
    poblacion = models.ForeignKey(PoblacionObjetivo, on_delete=models.PROTECT, null=True)
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT, null=True)
    detalles = models.TextField(verbose_name="Detalles", null=True,  blank=True)
    estatus = models.BooleanField(verbose_name=("Estatus"), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitud"

    def __str__(self):
        return self.nombre

class Configuracion(models.Model):
    carga = models.BooleanField(verbose_name=("Carga de solicitudes"), default=True)
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT, null=True, blank=True)
    fecha = models.DateField(verbose_name="Fecha proxima atención", null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Configuración"
        verbose_name_plural = "Configuraciones"

    def __str__(self):
        return str(self.id)

class RegistroImpresion(models.Model):
    solcitud = models.ForeignKey(Solicitud, on_delete=models.PROTECT, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete= models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Registro de impresiones"
        verbose_name_plural = "Registro de impresiones"

    def __str__(self):
        return str(self.id)
