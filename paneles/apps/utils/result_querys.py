import re
from rest_framework import serializers
from apps.home.serializers import ServicioSerializers, SolicitantesSerializers
from django.db.models import Q
from apps.home.models import *
from django.core.exceptions import ObjectDoesNotExist

def filterSolicitudes(ec="",dis="",sexo="",pob="",zona=""):
    consulta = Q()
    consulta = Q(estatus=True)
    if ec!="0":
        consulta &= Q(estcivil=ec)
    if pob!="0":
        poblacion =  PoblacionObjetivo.objects.get(pk=pob)
        consulta &= Q(poblacion=poblacion)
    if dis!="0":
        consulta &= Q(discapacidad=dis)
    if sexo!="0":
        consulta &= Q(sexo=sexo)
    if zona!="0":
        zonaa =  Zona.objects.get(pk=zona)
        consulta &= Q(zona=zonaa)
    solicitudes = Solicitud.objects.filter(consulta)
    return solicitudes

#validación existencia registro
def ValidacionCurp(curp):
    curp_tow = curp.upper().strip()
    try:
        existe = Solicitud.objects.get(curp = curp_tow)
    except ObjectDoesNotExist:
        return True
    print('ya existe un usuario con esa curp')
    return False

#Register Solicitud from api
def CreateNewSolicitud(solicitud, servicios):
    Newsolicitud = Solicitud()
    #serializer = SolicitantesSerializers(solicitud)
    if ValidacionCurp(solicitud['curp']):
        Newsolicitud.nombre = solicitud['nombre']
        Newsolicitud.appaterno = solicitud['appaterno']
        Newsolicitud.apmaterno = solicitud['apmaterno']
        Newsolicitud.curp = solicitud['curp']
        Newsolicitud.sexo = solicitud['sexo']
        Newsolicitud.estcivil = solicitud['estcivil']
        Newsolicitud.discapacidad = solicitud['discapacidad']
        Newsolicitud.domicilio = solicitud['domicilio']
        Newsolicitud.calle = solicitud['calle']
        Newsolicitud.exterior = solicitud['exterior']
        Newsolicitud.codigo = solicitud['codigo']
        Newsolicitud.correo = solicitud['correo']
        Newsolicitud.telefono = solicitud['telefono']
        Newsolicitud.detalles = solicitud['detalles']
        
        try:
            zona = Zona.objects.get(pk= solicitud['zona'])
        except ObjectDoesNotExist:
            print('fue la zona')
            return False
        Newsolicitud.zona = zona
            
        try:
            poblacionO = PoblacionObjetivo.objects.get(pk=solicitud['poblacion'])
        except ObjectDoesNotExist:
            print('fue la poblacion')
            return False
        Newsolicitud.poblacion = poblacionO
        Newsolicitud.save()
        try:
            reg_solicitud = Solicitud.objects.get(pk = Newsolicitud.pk)
        except ObjectDoesNotExist:
            print('fue el registro')
            return False
        for id_s in servicios:
            try:
                Object_servicio = ServiciosSolicitud.objects.get(pk=id_s)
            except ObjectDoesNotExist:
                print('Error al añadir los servicios')
                return False
            Newsolicitud.servicios.add(Object_servicio) 
        return True
    else:
        return False