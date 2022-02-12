from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('torneo/', torneo, name= "AppCoderTorneo"),
    path('inicio/', inicio, name="AppCoderInicio"),
    path('nadador/', nadador, name="AppCoderNadador"),
    path('prueba/', prueba, name="AppCoderPrueba"),
    path('formularioNadador/', formulario_nadador, name="AppCoderCursoFormulario"),



]