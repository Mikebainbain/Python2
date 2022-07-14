from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context

def saludo(request):
    doc_externo=open("C:/Users/ur513.dsi/Desktop/Proyectos_django/Proyecto1/Proyecto1/Plantillas/index.html") 
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento = plt.render( ctx)
    return HttpResponse(documento)

def Despedida(request):
    return HttpResponse("Adios django")

def Fecha(request):
    fecha_actual = datetime.now()

    documento = """<html>
    <body>
    <h1>Fecha y hora actual %s </h1>
    </body> 
    </html>""" %fecha_actual
    return  HttpResponse(documento)

def Calcularedad(request,edad,year):
    #edadActual= 25
    periodo = year - 2022
    edadFutura = edad+periodo
    documento = "<html><body><h1>En el año %s tendras %s años</h1></body></html>" %(year,edadFutura)

    return HttpResponse(documento)