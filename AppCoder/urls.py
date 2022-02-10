from django.urls import path
from AppCoder.views import torneo


urlpatterns = [
    path('torneo/', torneo),
]