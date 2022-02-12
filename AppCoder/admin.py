from django.contrib import admin

from AppCoder.models import Nadador, Prueba, Torneo

# Register your models here.
admin.site.register(Nadador)

admin.site.register(Torneo)

admin.site.register(Prueba)