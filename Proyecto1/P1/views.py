from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
#objeto persona
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido= apellido

def saludo(request): #primera vista
     #declaracion de objeto
    p1=Persona("Jose M.","Leon")
    temasCurso = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    #nombre = "Pedro"
    #apellido = "Perez"
    hoy = datetime.datetime.now()
    #doc_externo = open("C:/Users/aldo_/Documents/ProyectosDjango/Proyecto1/Proyecto1/plantillas/plantilla1.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #cargar plantillas con loader
    #doc_ext = get_template('plantilla1.html')
    #ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":hoy, 
    #    "temas": temasCurso})
    #documento = doc_ext.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":hoy,"temas": temasCurso})
    return render(request, "plantilla1.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":hoy,"temas": temasCurso})

def cursoC(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "cursoC.html", {"fecha":fecha_actual})

def cursoCSS(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "cursoCSS.html", {"fecha":fecha_actual})

def despedida(request):
    return HttpResponse("Adios")

def fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1> fecha y hora actual %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def edad(request,edad,agnio):
    periodo = agnio -2021
    edadActual = edad+periodo

    #documento = "<html><body><h1>En el año %s tendras %s años</h1></body></html>" %(agnio,edadActual)
    documento = "<html><body><h1><center>F"
    return HttpResponse(documento)
