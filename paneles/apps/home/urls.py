"""cartilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', InicioView.as_view(), name="inicio"),
    path('imprecion/solicitud/<str:ids>', ContratacionView.as_view(), name="imprimir"),
    path('estadisticas/servicios/<str:idz>', BeneficiosView.as_view(), name="beneficios"),
    path('estadisticas/servicios/imprimir/<str:idz>', ImprimirView.as_view(), name="imprimir"),
    path('estadisticas/servicios/detalles/<str:idz>', DetallesView.as_view(), name="detalles"),
    path('editar/<str:idsolicitud>', EditView.as_view(), name="editar"),
    path('duplicidad/<str:ids>', DuplicidadView.as_view(), name="duplicidad"),
    path('familiares/<str:ids>', FamiliaresView.as_view(), name="familia"),
]