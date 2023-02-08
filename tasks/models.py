from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    titulo=models.CharField(max_length=100, verbose_name='¿Cuál es la tarea?')
    descripcion=models.TextField(blank=True,verbose_name='Agrega una descripción:')
    fechacreacion=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField(null=True,verbose_name='Ingresa el deadline de la tarea')
    importante=models.BooleanField(default=False,verbose_name='¿Es importante?')
    completada=models.BooleanField(default=False,verbose_name='¿Ya completaste la tarea?')
    autor=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo + '  - by ' + self.autor.username