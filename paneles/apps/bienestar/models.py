from django.db import models

# Create your models here.
class Adicional(models.Model):
    folio = models.CharField(  max_length=200, verbose_name="Folio")
    solicitud = models.CharField(max_length=200, verbose_name="Id Solicitud")
    name_attended = models.CharField(  max_length=200, verbose_name="Nombre")
    total_people = models.CharField(  max_length=200, verbose_name="Habitantes")
    disability = models.CharField(  max_length=200, verbose_name="personas con discapacidad")
    mom = models.CharField(  max_length=200, verbose_name="madres solteras")
    adult = models.CharField(  max_length=200, verbose_name="adultos mayores")
    younger = models.CharField(  max_length=200, verbose_name="menores de edad")
    house = models.CharField(  max_length=200, verbose_name="Casa")
    ceiling = models.CharField(  max_length=200, verbose_name="Techo")
    floor = models.CharField(  max_length=200, verbose_name="Piso")
    bath = models.CharField(  max_length=200, verbose_name="Baño")
    estatus = models.BooleanField(verbose_name=("Estatus"), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "Información Bienestar"
        verbose_name_plural = "Información Bienestar"

    def __str__(self):
        return self.folio