from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    types=(
        ('s', 'Super usuario'),
        ('a', 'Administrador'),
        ('u', 'Usuario'),
        
    )
    tipoUsuario = models.CharField(max_length=30,choices=types, verbose_name='Tipo de usuario')
    #The auto_now_add will set the timezone.now() only when the instance is created, 
    # and auto_now will update the field everytime the save method is called.
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username