from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template # Gracias a esta importacion no son necesarias las lineas 24,25,26  pero se debe especificar la ruta de las plantillas en settings .py -> TEMPLATES
from django.shortcuts import render # con esto nos evitamos las demas importaciones de la linea 2 a la 4  y tambien no necesitamos la linea 28

# Constructor
class Persona(object):
    def __init__(self, nombre, apellido):
        # Propiedades
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):

    p1 = Persona("Angel", "Barrera") # variable asignada a el constructor

    nombre = "Miguel" 
    apellido = "Lopez"
    edad = 25
    val_fun_fecha = datetime.now()  #se puede colocar el valor que le queremos asignar directamente  osea a lado de el valor clave
    tema = ["Cocina","Tecnologia","Noticias","Cultura"]
    tema2 = []
    
  # doc_externo=open("C:/Users/ur513.dsi/Desktop/Proyectos_django/Proyecto1/Proyecto1/Plantillas/index.html") 
  # plt=Template(doc_externo.read())
  # doc_externo.close()
  #  doc_externo = get_template('index.html')
  # ctx=Context({"val_nombre": p1.nombre,"val_apellido":p1.apellido , "val_edad": edad, "val_fecha" :val_fun_fecha , "temas":tema,"ots_temas":tema2}) el metodo render recibe un template del metodo get_template  diferente ala conversion que se hacia con anterioridad
    #documento = doc_externo.render({"val_nombre": p1.nombre,"val_apellido":p1.apellido , "val_edad": edad, "val_fecha" :val_fun_fecha , "temas":tema,"ots_temas":tema2}) 
      
    return render(request,"index.html",{"val_nombre": p1.nombre,"val_apellido":p1.apellido , "val_edad": edad, "val_fecha" :val_fun_fecha , "temas":tema,"ots_temas":tema2})




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