from django.contrib import admin
from .models import *

# Register your models here.
class ServiciosAdmin(admin.ModelAdmin):
    list_display=['id','nombre','direccion']
    list_display_links=['id','nombre']
    search_fields=['nombre','direccion__nombre']

admin.site.register(ServiciosSolicitud,ServiciosAdmin)

class DireccionAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(Direccion,DireccionAdmin)

class SolicitudAdmin(admin.ModelAdmin):
    list_display=['id','nombre', 'created', 'zona']
    list_display_links=['id','nombre']
    search_fields=['nombre', 'id', 'zona__nombre']
    filter_horizontal = ('servicios',)

admin.site.register(Solicitud,SolicitudAdmin)

class PoblacionAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(PoblacionObjetivo,PoblacionAdmin)

class ConfiguracionAdmin(admin.ModelAdmin):
    list_display=['id']
    list_display_links=['id']
    search_fields=['id']

admin.site.register(Configuracion,ConfiguracionAdmin)

class ZonaAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre',]

admin.site.register(Zona, ZonaAdmin)

class RegistroAdmin(admin.ModelAdmin):
    list_display=['id','solcitud', 'usuario']
    list_display_links=['id','solcitud', 'usuario']
    search_fields=['solcitud', 'usuario']

admin.site.register(RegistroImpresion, RegistroAdmin)