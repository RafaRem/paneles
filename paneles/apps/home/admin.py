from django.contrib import admin
from .models import *

# Register your models here.
class ServiciosAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(ServiciosSolicitud,ServiciosAdmin)

class DireccionAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(Direccion,DireccionAdmin)

class SolicitudAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']
    filter_horizontal = ('servicios',)

admin.site.register(Solicitud,SolicitudAdmin)

class PoblacionAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(PoblacionObjetivo,PoblacionAdmin)