from rest_framework import serializers

class SolicitantesSerializers(serializers.Serializer):
    nombre = serializers.CharField(  max_length=100)
    appaterno = serializers.CharField(  max_length=100)
    apmaterno = serializers.CharField(  max_length=100)
    curp = serializers.CharField(  max_length=50)
    estcivil = serializers.CharField(  max_length=50)
    discapacidad =serializers.CharField(  max_length=50)
    domicilio = serializers.CharField(  max_length=100)
    calle = serializers.CharField(  max_length=50)
    exterior = serializers.CharField(  max_length=50)
    codigo = serializers.CharField(  max_length=50)
    correo = serializers.CharField(  max_length=200)
    telefono = serializers.CharField(  max_length=200)
    sexo = serializers.CharField(  max_length=50)
    poblacion = serializers.CharField(max_length=140)
    zona = serializers.CharField(max_length=140)
    detalles = serializers.CharField()
    estatus = serializers.BooleanField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()      

#serializers Servicios
class ServicioSerializers(serializers.Serializer):
    nombre = serializers.CharField(  max_length=200,)
    direccion = serializers.CharField()
    estatus = serializers.BooleanField()
    seguimiento = serializers.BooleanField()
    limite = serializers.BooleanField()
    cantidad = serializers.CharField()
  
    