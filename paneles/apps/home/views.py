from re import S
from django.shortcuts import render, HttpResponseRedirect, redirect
import json
from django.views.generic import  View
import datetime
from datetime import date
from django.urls import reverse
from .models import *
from django.db.models import Q

from django.core.mail import send_mail 
from django.conf import settings


def RegistroImpresionHistorial(request, ids):
  
    solicitud = Solicitud.objects.filter(pk=ids, estatus=True)
    registro = RegistroImpresion()
  
    if len(solicitud)>0:
        solicitud = solicitud[0]
        registro.solcitud = solicitud
        registro.usuario = request.user
        registro.save()
        url = reverse('imprimir',  kwargs={'ids':solicitud.pk})
        return redirect(url)   
    else: 
        url = reverse('imprimir',  kwargs={'ids':'0'})
        return redirect(url)

class InicioView(View):
    
    def curps(self):
        array=[]
        solicitudes = Solicitud.objects.filter(estatus=True)
        for solicitud in solicitudes:
            array.append([solicitud.curp])
        return array

    def descontar(self, servicio):
        configuracion =Configuracion.objects.get(pk=1)
        if servicio.limite:
            if int(servicio.cantidad) > 0:
                solicitudes = Solicitud.objects.filter(zona=configuracion.zona, servicios__in=[servicio])
                total = len(solicitudes) +1
                if int(servicio.cantidad) <= total:
                    servicio.cantidad = 0
                    servicio.save()
            else:
                return False
        return True
    
    def get(self,request):
        configuracion = Configuracion.objects.filter(pk=1)
        if len(configuracion) > 0:
            configuracion = configuracion[0]
            if configuracion.carga == True:
                if request.user.is_authenticated:
                    zonas = Zona.objects.filter(estatus=True)
                    servicios = ServiciosSolicitud.objects.filter(estatus=True)
                    solicitudes = self.curps()
                    solicitudes = json.dumps(solicitudes)
                    direcciones = Direccion.objects.all()
                    poblaciones = PoblacionObjetivo.objects.filter(estatus=True)
                    return  render(request,  "home/inicio.html",{'servicios':servicios,
                    'direcciones':direcciones, 'poblaciones': poblaciones, 'solicitudes':solicitudes,'zonas': zonas} )
                else:
                    url = reverse('login')
                    return redirect(url)
            else:
                return  render(request,  "home/inicio.html" )
        else:
            return  render(request,  "home/inicio.html" )

    def post(self,request):
        if request.user.is_authenticated:
            verificacion = Solicitud.objects.filter(curp =request.POST.get('curp'), estatus=True) 
            
            if len(verificacion) == 0:
                solicitud = Solicitud()
                solicitud.nombre = request.POST.get('nombre')
                solicitud.appaterno = request.POST.get('paterno')
                solicitud.apmaterno = request.POST.get('materno')
                solicitud.curp = request.POST.get('curp')
                solicitud.sexo = request.POST.get('curp')[10:11]
                solicitud.estcivil = request.POST.get('estcivil')
                solicitud.discapacidad = request.POST.get('discapacidad')
                solicitud.domicilio = request.POST.get('domicilio')
                solicitud.calle = request.POST.get('calle')
                solicitud.exterior = request.POST.get('exterior')
                solicitud.codigo = request.POST.get('cp')
                solicitud.correo = request.POST.get('email')
                solicitud.telefono = request.POST.get('telefono')
                solicitud.detalles = request.POST.get('observacion')
                zona = Zona.objects.get(pk= request.POST.get('zona'))
                solicitud.zona = zona
                if request.POST.get('poblacion') != 0:
                    poblacionO = PoblacionObjetivo.objects.get(pk=request.POST.get('poblacion'))
                    solicitud.poblacion = poblacionO
                solicitud.save()
                #Servicios
                
                if request.POST.get('servicio') != "x":
                    servicio1 = ServiciosSolicitud.objects.get(pk=request.POST.get('servicio'))
                    self.descontar(servicio=servicio1)
                    solicitud.servicios.add(servicio1)  
                if request.POST.get('servicio2') != "x":
                    servicio2= ServiciosSolicitud.objects.get(pk=request.POST.get('servicio2'))
                    self.descontar(servicio=servicio2)
                    solicitud.servicios.add(servicio2)
                if request.POST.get('servicio3') != "x":
                    servicio3= ServiciosSolicitud.objects.get(pk=request.POST.get('servicio3'))
                    self.descontar(servicio=servicio3)
                    solicitud.servicios.add(servicio3)
                '''
                familiar = FamiliaresView.ValidarFamiliar(paterno=request.POST.get('paterno'),sexo=request.POST.get('curp')[10:11],materno=request.POST.get('materno'),calle=request.POST.get('calle'),codigo=request.POST.get('cp'),exterior=request.POST.get('externo') )
                print("familiar", len(familiar))
                if len(familiar) > 0:
                    url = reverse('familia', kwargs={'ids':solicitud.pk})
                    print(url)
                    return redirect(url)
                else:'''
                url = reverse('imprimir', kwargs={'ids':solicitud.pk})
                return redirect(url)
            else:
                idVerificacion = verificacion[0]
                url = reverse('duplicidad', kwargs={'ids':idVerificacion.pk})
                return redirect(url)
        else:
            url = reverse('login')
            return redirect(url)

#Reimpreción de solicitudes 
class ContratacionView(View):
    def get(self,request, ids=""):
        if ids != "0":
            solicitud = Solicitud.objects.get(pk=ids)
            servicios = solicitud.servicios.all()
            folio = str(solicitud.pk).zfill(4)
            fecha = solicitud.created.date()
            return  render(request,  "home/proceso.html",{'solicitud':solicitud,'servicios': servicios, 'id': ids, 'folio': folio, 'fecha': fecha, 'carga': False})
        else: 
           return  render(request,  "home/proceso.html",{'id':ids})
    def post(self,request, ids=""):
        curp = request.POST.get('curp')
        solicitud = Solicitud.objects.filter(curp=curp, estatus=True)
        if len(solicitud)>0:
            solicitud = solicitud[0]
            servicios = solicitud.servicios.all()
            folio = "FB-"+str(solicitud.pk).zfill(6)
            fecha = solicitud.created.date()
            return  render(request,  "home/proceso.html",{'solicitud':solicitud,'servicios': servicios, 'id': solicitud.pk, 'folio': folio, 'fecha': fecha, 'carga': False})   
        else: 
           mensaje = True 
           return  render(request,  "home/proceso.html",{'id':"0", 'mns':mensaje})

#Apartedo de estadistica
class BeneficiosView(View):
    def ObtenerEstadisticaPoblacion(self, idz):
        poblacion = []
        poblacionObjetivo = PoblacionObjetivo.objects.filter(estatus=True)
        if idz == "0":
            zona = Configuracion.objects.get(pk=1)
            zona = zona.zona
        else:
            zona = Zona.objects.get(pk=idz)
        for pob in poblacionObjetivo:
            if idz == "0":
                cantidad = Solicitud.objects.filter(poblacion=pob, estatus=True)
            else:
                cantidad = Solicitud.objects.filter(poblacion=pob, estatus=True, zona=zona)
            poblacion.append({
               'poblacion': pob,
               'cantidad': len(cantidad) 
            })
        return poblacion

    def get(self,request,idz="0"):
        direcciones =Direccion.objects.all()
        poblacionObjetivo = self.ObtenerEstadisticaPoblacion(idz=idz)
        if idz == "0":
            zona = Configuracion.objects.get(pk=1)
            zona = zona.zona
        else:
            zona = Zona.objects.get(pk=idz)
        
        total =0
        arraytotal = []
        mujeres = 0
        hombres = 0
    
        zonas = Zona.objects.all()
        for direccion in direcciones:
            servicios = ServiciosSolicitud.objects.filter(direccion= direccion)
            array = []
            total =0
            
            for servicio in servicios:
                if idz == "0":
                    query = Solicitud.objects.filter(servicios__id =servicio.pk, estatus=True) 
                else:
                    query = Solicitud.objects.filter(servicios__id =servicio.pk, estatus=True, zona=zona) 
                array.append({
                    'cantidad': len(query),
                    'servicio': servicio
                })
                total += len(query)
            arraytotal.append({'direccion':direccion,
            'servicios':array,
            'total': total })

            if idz == "0":
                solicitudes_total = Solicitud.objects.filter(estatus=True)
                hombres = Solicitud.objects.filter(sexo='H',estatus=True)
                mujeres = Solicitud.objects.filter(sexo='M',estatus=True)
                discapacidades = Solicitud.objects.filter(~Q(discapacidad='n'), estatus=True)
                localidad = 'Todas las Dependencias'
            else:
                discapacidades = Solicitud.objects.filter(~Q(discapacidad='n'), estatus=True, zona=zona)
                solicitudes_total = Solicitud.objects.filter(estatus=True, zona=zona)
                hombres = Solicitud.objects.filter(sexo='H',estatus=True, zona=zona)
                mujeres = Solicitud.objects.filter(sexo='M',estatus=True, zona=zona)
                localidad =zona.nombre.upper()
        return  render(request,  "home/beneficios.html", {
        'estadisticas': arraytotal,
        'total_solicitudes': len(solicitudes_total),
        'hombres': len(hombres),
        'mujeres': len(mujeres),
        'poblacion': poblacionObjetivo,
        'discapacidades':len(discapacidades),
        'zonas': zonas,
        'localidad':localidad,
        'idz':idz})
    def post(self,request):
        return  render(request,  "home/beneficios.html")

#Editar datos generales del solicitante
class EditView(View):
    def get(self,request,idsolicitud=""):
        if idsolicitud == "0":
            url = reverse('imprimir', kwargs={'ids':"0"})
            return redirect(url)
        solicitud = Solicitud.objects.get(pk=idsolicitud)
        poblaciones = PoblacionObjetivo.objects.all()
        return  render(request,  "home/editar.html",{'solicitud':solicitud, 'poblaciones': poblaciones} )
    def post(self,request,idsolicitud=""):
        solicitud = Solicitud.objects.get(pk=idsolicitud)
        solicitud.nombre = request.POST.get('nombre')
        solicitud.appaterno = request.POST.get('paterno')
        solicitud.apmaterno = request.POST.get('materno')
        solicitud.curp = request.POST.get('curp')
        solicitud.estcivil = request.POST.get('estcivil')
        solicitud.discapacidad = request.POST.get('discapacidad')
        solicitud.domicilio = request.POST.get('domicilio')
        solicitud.calle = request.POST.get('calle')
        solicitud.exterior = request.POST.get('exterior')
        solicitud.codigo = request.POST.get('cp')
        solicitud.correo = request.POST.get('email')
        solicitud.telefono = request.POST.get('telefono')
        solicitud.detalles = request.POST.get('observacion')
        if request.POST.get('poblacion') != 0:
            poblacionO = PoblacionObjetivo.objects.get(pk=request.POST.get('poblacion'))
            solicitud.poblacion = poblacionO
        solicitud.save()
        #Servicios
        url = reverse('imprimir', kwargs={'ids':solicitud.pk})
        return redirect(url)

class DuplicidadView(View):
    def get(self,request,ids=""):
        solicitud = Solicitud.objects.get(pk=ids)
        return  render(request,  "home/duplicidad.html",{'solicitud':solicitud} )
    def post(self,request,ids=""):
        solicitud = Solicitud.objects.get(pk=ids)
        return  render(request,  "home/duplicidad.html",{'solicitud':solicitud} )

class FamiliaresView(View):
    def ValidarFamiliar(self,paterno, materno,sexo, calle, codigo, exterior):
        familiares =[]
        vcalle = False
        vcodigo = False
        vexterno = False
        vapellido = False
        solicitudes = Solicitud.objects.filter(estatus=True)
        for solicitud in solicitudes:
            verificacion = 0
            if solicitud.exterior == exterior:
                vexterno= True
                verificacion += 1
            if solicitud.calle == calle:
                vcalle= True
                verificacion += 1
            if solicitud.codigo == codigo:
                vcodigo=True
                verificacion += 1
            if solicitud.appaterno == paterno:
                vapellido = True
                verificacion += 1
            if verificacion >= 3:
                familiares.append({'solicitud':solicitud,'apellido':vapellido, 'codigo':vcodigo, 'calle':vcalle, 'exterior':vexterno})
        
        return familiares


    def get(self,request,ids=""):
        solicitud = Solicitud.objects.get(pk=ids)
        familiar = self.ValidarFamiliar(paterno=solicitud.appaterno,sexo=solicitud.sexo,materno=solicitud.apmaterno,calle=solicitud.calle,codigo=solicitud.codigo,exterior=solicitud.exterior )
        return  render(request,  "home/familiares.html",{'solicitud':solicitud,'familiares':familiar} )
    def post(self,request,ids=""):
        solicitud = Solicitud.objects.get(pk=ids)
        return  render(request,  "home/duplicidad.html",{'solicitud':solicitud} )


class ImprimirView(View):
    def ObtenerEstadisticaPoblacion(self, idz):
        poblacion = []
        poblacionObjetivo = PoblacionObjetivo.objects.all()
        if idz == "0":
            zona = Configuracion.objects.get(pk=1)
            zona = zona.zona
        else:
            zona = Zona.objects.get(pk=idz)
        for pob in poblacionObjetivo:
            if idz == "0":
                cantidad = Solicitud.objects.filter(poblacion=pob, estatus=True)
            else:
                cantidad = Solicitud.objects.filter(poblacion=pob, estatus=True, zona=zona)
            poblacion.append({
               'poblacion': pob,
               'cantidad': len(cantidad) 
            })
        return poblacion

    def get(self,request,idz="0"):
        direcciones =Direccion.objects.all()
        poblacionObjetivo = self.ObtenerEstadisticaPoblacion(idz=idz)
        if idz == "0":
            zona = Configuracion.objects.get(pk=1)
            zona = zona.zona
        else:
            zona = Zona.objects.get(pk=idz)
        
        total =0
        arraytotal = []
        mujeres = 0
        hombres = 0
    
        zonas = Zona.objects.all()
        for direccion in direcciones:
            servicios = ServiciosSolicitud.objects.filter(direccion= direccion)
            array = []
            total =0
            
            for servicio in servicios:
                if idz == "0":
                    query = Solicitud.objects.filter(servicios__id =servicio.pk, estatus=True) 
                else:
                    query = Solicitud.objects.filter(servicios__id =servicio.pk, estatus=True, zona=zona) 
                array.append({
                    'cantidad': len(query),
                    'servicio': servicio
                })
                total += len(query)
            arraytotal.append({'direccion':direccion,
            'servicios':array,
            'total': total })

            if idz == "0":
                solicitudes_total = Solicitud.objects.filter(estatus=True)
                hombres = Solicitud.objects.filter(sexo='H',estatus=True)
                mujeres = Solicitud.objects.filter(sexo='M',estatus=True)
                discapacidades = Solicitud.objects.filter(~Q(discapacidad='n'), estatus=True)
                localidad = 'Todas las Dependencias'
            else:
                discapacidades = Solicitud.objects.filter(~Q(discapacidad='n'), estatus=True, zona=zona)
                solicitudes_total = Solicitud.objects.filter(estatus=True, zona=zona)
                hombres = Solicitud.objects.filter(sexo='H',estatus=True, zona=zona)
                mujeres = Solicitud.objects.filter(sexo='M',estatus=True, zona=zona)
                localidad =zona.nombre.upper()
        return  render(request,  "home/imprecion.html", {'estadisticas': arraytotal,
        'total_solicitudes': len(solicitudes_total),
        'hombres': len(hombres),
        'mujeres': len(mujeres),
        'poblacion': poblacionObjetivo,
        'discapacidades':len(discapacidades),
        'zonas': zonas,
        'localidad':localidad,
        'idz':idz})
    def post(self,request):
        return  render(request,  "home/beneficios.html")


class DetallesView(View):
    def get(self,request,idz=""):
        if request.user.is_authenticated:
            if idz == "" or idz == "0":
                localidad = "Todas las Localidades"
                solicitudes = Solicitud.objects.filter(estatus=True)
            else:
                zona = Zona.objects.get(pk=idz)
                localidad = zona.nombre.upper()
                solicitudes = Solicitud.objects.filter(zona=zona, estatus=True)
            arraySolicitudes = []
            total_servicios = 0
            total_personas = len(solicitudes)
            zonas = Zona.objects.all()
            for solicitud in solicitudes:
                cantidad= solicitud.servicios.all()
                total_servicios += len(cantidad)
                arraySolicitudes.append({'nombre': solicitud.nombre+" "+solicitud.appaterno+" "+solicitud.apmaterno,
                'poblacion': solicitud.poblacion,
                'discapacidad': solicitud.discapacidad,
                'cantidad': len(cantidad),
                'servicios':cantidad})
            return  render(request,  "home/detalles_solicitud.html",{'solicitudes':arraySolicitudes, 'localidad': localidad, 
            'total_servicios': total_servicios, 'total': total_personas, 'zonas': zonas, 'localidad': localidad})
        else:
            url = reverse('inicio')
            return redirect(url)

    def post(self,request):
        return  render(request,  "home/detalles_solicitud.html")


class NewServicesView(View):
    def get(self,request,ids=""):
        solicitud = Solicitud.objects.get(curp=ids)
        servicios = ServiciosSolicitud.objects.filter(estatus=True)
        direcciones = Direccion.objects.all()
        before_services = solicitud.servicios.all()
        servicio1 = {'direccion': '', 'id': ''}
        servicio2 = {'direccion': '', 'id': ''}
        servicio3 = {'direccion': '', 'id': ''}
        for idx, val in enumerate(before_services):
            print(val.direccion.id)
            if idx == 0:
                servicio1['id'] = val.id
                servicio1['direccion'] = val.direccion.id
            if idx == 1:
                servicio2['id'] = val.id
                servicio2['direccion'] = val.direccion.id
            if idx == 2:
                servicio3['id'] = val.id
                servicio3['direccion'] = val.direccion.id

        return  render(request,  "home/newservices.html",{'servicios':servicios,
        'direcciones':direcciones, 'before_services': before_services, 'solicitud':solicitud, 
        'serv_1':servicio1, 'serv_2':servicio2, 'serv_3':servicio3} )



    def post(self,request,ids=""):
        solicitud = Solicitud.objects.get(curp=ids)
        servicios = solicitud.servicios.all()
        if len(servicios) > 0:
            for servicio in servicios:
                solicitud.servicios.remove(servicio.pk)
        '''ya se han eliminado los antiguos servicios
            se añadiran los nuevos servicos
        '''
        inicio = InicioView()
        if request.POST.get('servicio') != "x":
            servicio1 = ServiciosSolicitud.objects.get(pk=request.POST.get('servicio'))
            inicio.descontar(servicio=servicio1)
            solicitud.servicios.add(servicio1)  
        if request.POST.get('servicio2') != "x":
            servicio2= ServiciosSolicitud.objects.get(pk=request.POST.get('servicio2'))
            inicio.descontar(servicio=servicio2)
            solicitud.servicios.add(servicio2)
        if request.POST.get('servicio3') != "x":
            servicio3= ServiciosSolicitud.objects.get(pk=request.POST.get('servicio3'))
            inicio.descontar(servicio=servicio3)
            solicitud.servicios.add(servicio3)
        url = reverse('imprimir', kwargs={'ids':solicitud.pk})
        return redirect(url)