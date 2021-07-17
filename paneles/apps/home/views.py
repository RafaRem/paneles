from django.shortcuts import render, HttpResponse, redirect

from django.views.generic import  View
import datetime
from datetime import date
from django.urls import reverse
from .models import *

#import Email
from django.core.mail import send_mail 
from django.conf import settings
# Create your views here.

def email(request):

    subject = 'Bienvenido a la Junta de Reclutamiento'
    message = 'su cita ha sido registrada en nuestro citio presentarse mañana porfis'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['rrembao00@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return True


class InicioView(View):
    def get(self,request):
        servicios = Servicios.objects.all()
        return  render(request,  "home/inicio.html",{'servicios':servicios} )
    def post(self,request):
        return  render(request, "home/inicio.html")

class ContratacionView(View):
    def get(self,request):
        
        return  render(request,  "home/proceso.html")
    def post(self,request):
            return  render(request,  "home/proceso.html")

class BeneficiosView(View):
    def get(self,request):
        return  render(request,  "home/beneficios.html")
    def post(self,request):
        return  render(request,  "home/beneficios.html")