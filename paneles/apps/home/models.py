from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Servicios(models.Model):
    titulo = models.CharField(  max_length=200, verbose_name="Titulo")
    subtitulo = models.TextField(verbose_name="Sub-Titulo")
    descripcion = RichTextField(verbose_name=("Descripción"))
    estatus = models.BooleanField(verbose_name=("Estatus"))
    imagen = models.ImageField(null=True, verbose_name=("Imagen"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.titulo