from django.db import models

# Create your models here.
class Torneo(models.Model):

    nombre = models.CharField(max_length=100)
    Fecha = models.DateField()
    lugar = models.CharField(max_length=50)


class Nadador(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()


class Prueba(models.Model):

    estilo = models.CharField(max_length=40)
    distancia = models.IntegerField()
    tiempos = models.IntegerField()
    