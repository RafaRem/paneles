from django.contrib import admin
from .models import *

# Register your models here.
class ServiciosAdmin(admin.ModelAdmin):
    list_display=['id','titulo']
    list_display_links=['id','titulo']
    search_fields=['titulo']

admin.site.register(Servicios,ServiciosAdmin)