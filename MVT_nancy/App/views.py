from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar
from django.shortcuts import render


from App.models import Familiar
from django.template import loader
from django.template import Template, Context

from django.utils import timezone

# Create your views here.

def MVT(request):
    #dato = Familiar(nombre= "Laura", edad = "40", fecha_nacimiento = "1982-02-08", apellido = "Rojas")
    #dato.save()
    familia_lista = Familiar.objects.all()
    return render(request, "MVT_NancyVR.html", {"familia": familia_lista})