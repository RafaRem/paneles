from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="nombre")
    stock =models.CharField(max_length=255, verbose_name="stock")
   
    class Meta:
        verbose_name = "productos"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre
