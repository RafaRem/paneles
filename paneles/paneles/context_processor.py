import os
from apps.home.models import Configuracion
from django.conf import settings

def add_variable_context(request):
   
    
    return{
        
        'settings': settings
    }