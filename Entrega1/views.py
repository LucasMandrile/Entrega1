from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
	return HttpResponse("Hola Django - Coder")

def template1(request):
    context = {"curso":"Python"}

    return render(request,"template1.html",context)

