from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('accounts/login', Login.as_view(), name="login"),
    path('logout',login_required( logoutUsuario), name="cerrar"),    
]