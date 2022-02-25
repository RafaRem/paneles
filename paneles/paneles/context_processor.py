import os
from apps.home.models import Configuracion
from django.conf import settings

def add_variable_context(request):
    configuracion = Configuracion.objects.filter(pk=1)
    if len(configuracion)> 0:
        return{
            'configuracion': configuracion[0],
            'settings': settings
        }
    else:
        return{
            'settings': settings
        }