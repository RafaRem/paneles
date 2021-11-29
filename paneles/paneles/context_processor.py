import os
from apps.home.models import Configuracion
from django.conf import settings

def add_variable_context(request):
    configuracion = Configuracion.objects.get(pk=1)
    return{
        'configuracion': configuracion,
        'settings': settings
    }