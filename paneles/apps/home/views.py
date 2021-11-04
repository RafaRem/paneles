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
        servicios = ServiciosSolicitud.objects.all()
        direcciones = Direccion.objects.all()
        return  render(request,  "home/inicio.html",{'servicios':servicios,
        'direcciones':direcciones} )
    def post(self,request):
        print("post")
        solicitud = Solicitud()
        solicitud.nombre = request.POST.get('nombre')
        solicitud.appaterno = request.POST.get('paterno')
        solicitud.apmaterno = request.POST.get('materno')
        solicitud.curp = request.POST.get('curp')
        solicitud.estcivil = request.POST.get('estcivil')
        solicitud.discapacidad = request.POST.get('discapacidad')
        solicitud.domicilio = request.POST.get('domicilio')
        solicitud.correo = request.POST.get('email')
        solicitud.telefono = request.POST.get('telefono')
        solicitud.save()
        #Servicios
        print(request.POST.get('servicio'))
        servicio1 = ServiciosSolicitud.objects.get(pk=request.POST.get('servicio'))
        servicio2= ServiciosSolicitud.objects.get(pk=request.POST.get('servicio2'))
        servicio3= ServiciosSolicitud.objects.get(pk=request.POST.get('servicio3'))
        print(servicio1)
        solicitud.servicios.add(servicio1)
        solicitud.servicios.add(servicio2)
        solicitud.servicios.add(servicio3)
        
        url = reverse('imprimir')
        return redirect(url+"/"+str(solicitud.pk))

class ContratacionView(View):
    def get(self,request, ids=""):
        if ids != "0":
            solicitud = Solicitud.objects.get(pk=ids)
            servicios = solicitud.servicios.all()
            return  render(request,  "home/proceso.html",{'solicitud':solicitud,'servicios': servicios})
        else: 
            servicios = ServiciosSolicitud.objects.all()
            direcciones = Direccion.objects.all()
            return  render(request,  "home/inicio.html",{'servicios':servicios,
            'direcciones':direcciones} )
    def post(self,request):
            return  render(request,  "home/proceso.html")

class BeneficiosView(View):
    def get(self,request):
        return  render(request,  "home/beneficios.html")
    def post(self,request):
        return  render(request,  "home/beneficios.html")