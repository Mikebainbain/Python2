from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context

# Constructor
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):

    p1=Persona("Angel", "Barrera")

    nombre = "Miguel" 
    apellido = "Lopez"
    edad = 25
    val_fun_fecha = datetime.now()  #se puede colocar el valor que le queremos asignar directamente  osea a lado de el valor clave
    
    doc_externo=open("C:/Users/ur513.dsi/Desktop/Proyectos_django/Proyecto1/Proyecto1/Plantillas/index.html") 
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"val_nombre": p1.nombre,"val_apellido":p1.apellido , "val_edad": edad, "val_fecha" :val_fun_fecha })
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