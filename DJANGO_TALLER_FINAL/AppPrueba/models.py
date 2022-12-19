from unittest.util import _MAX_LENGTH
from django.db import models
from .elecciones import lista

# Create your models here.

class Institucion(models.Model):
    institucion = models.CharField(max_length = 50)
    def __str__(self):
        return self.institucion

class Inscritos(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 30)
    fechaInscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete = models.CASCADE)
    horainscripcion = models.TimeField()
    estado = models.CharField(max_length= 50, choices= lista)
    observacion = models.CharField(max_length = 50, blank= True)
