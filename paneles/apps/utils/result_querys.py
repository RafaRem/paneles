from apps.home.serializers import ServicioSerializers, SolicitantesSerializers
from django.db.models import Q
from apps.home.models import *


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