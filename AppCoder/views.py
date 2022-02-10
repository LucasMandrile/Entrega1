from django.shortcuts import render

# Create your views here.
def torneo(request):
    return render(request, 'AppCoder/torneo.html')