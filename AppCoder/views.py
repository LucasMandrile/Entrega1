from django.shortcuts import render
from .models import Nadador
from AppCoder.forms import FormularioNadador

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
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_nombre = informacion['nombre']
            #r_apellido = informacion['apellido']
            r_email = informacion['email']
            r_edad = informacion['edad']
        
            nadador = Nadador(nombre=r_nombre,email=r_email, edad=r_edad)
            nadador.save()
    
    miFormulario = FormularioNadador()

    return render(request, 'AppCoder/formularioNadador.html',{"miFormulario":miFormulario})




     