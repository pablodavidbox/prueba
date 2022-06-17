from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader


def probandoTemplate(self):
    # miHtml = open("C:\Users\pablo\OneDrive\Escritorio\MVT\MVT_coderhouse\MVT_nancy\MVT_nancy\plantillas")
    ##plantilla = Template(miHtml.read())
    plantilla = loader.get_template('MVT_NancyVR.html')
    # miHtml.close()
    ##miContexto = Context()
    ##documento = plantilla.render(miContexto)
    documento = plantilla.render()
    return HttpResponse(documento)


def home(request):
    return HttpResponse("<h1>Hola Este es el MVT de Nancy Villena selecciona: http://127.0.0.1:8000/MVT para acceder al ejercicio </h1>")
