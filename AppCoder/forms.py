from django import forms

class FormularioNadador(forms.Form):

    nombre = forms.CharField(max_length=40)
    #apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    edad = forms.IntegerField()