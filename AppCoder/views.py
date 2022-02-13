import re
from django.shortcuts import render,redirect

from .models import Nadador
from AppCoder.forms import FormularioNadador
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def torneo(request):
    return render(request, 'AppCoder/torneo.html')

def nadador(request):
    return render(request, 'AppCoder/nadador.html')

def prueba(request):
    return render(request, 'AppCoder/prueba.html')

def formulario_nadador(request):
    if request.method == 'POST':

        miFormulario = FormularioNadador(request.POST)
        
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_nombre = informacion['nombre']
            #r_apellido = informacion['apellido']
            r_email = informacion['email']
            r_edad = informacion['edad']
        
            nadador = Nadador(nombre=r_nombre,email=r_email, edad=r_edad)
            nadador.save()

            return redirect("AppCoderNadador")
    
    miFormulario = FormularioNadador()

    return render(request, 'AppCoder/FormularioNadador.html',{"miFormulario":miFormulario})

def busqueda_nadador(request):
    return render(request, 'AppCoder/busquedaNadador.html')
 
def buscar(request):

    if request.GET["nombre"]:
    #respuesta = f"Estoy buscando al nadador: {request.GET ['nadador']} "
        nombre = request.GET["nombre"]

        print(f"el nombre es: {nombre}")

        nadadores= Nadador.objects.filter(nombre=nombre)

        return render(request,'AppCoder/resultadoBusqueda.html',{"nadadores":nadadores,"nombre":nombre})
    else:

        respuesta= "No enviaste datos"

    return HttpResponse(respuesta)




     