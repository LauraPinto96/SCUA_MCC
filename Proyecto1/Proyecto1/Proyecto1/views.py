from ast import Return
from contextvars import Context
from re import template
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #primera vista
    p1=Persona("UIS", "Bucaramanga Colombia")

    #nombre= "Julián"
    #apellido="Rodíguez"

    temasDelCurso=["Altura","Aceleración","Estado de eyección", "Camaras","Localización GPS", "Giroscopio", "Estado de la misión", "Temperaturas"]
    ahora=datetime.datetime.now()

#cargar plantilla de forma manual
    #doc_externo=open("C:/Users/LENOVO/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

#lectura del documento cargado
   # plt=Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo=loader.get_template('miplantilla.html')

    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso })

#renderisado
    #documento=plt.render(ctx)

    #documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso })

    #return HttpResponse(documento)
    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso })

def cursoC(request):
     fecha_actual=datetime.datetime.now()
     return render(request, "cursoC.html", {"dameFecha":fecha_actual})

def cursoCss(request):
     fecha_actual=datetime.datetime.now()
     return render(request, "cursoCss.html", {"dameFecha":fecha_actual})

def Altura(request):
     fecha_actual=datetime.datetime.now()
     return render(request, "Altura.html", {"dameFecha":fecha_actual})

def camaras(request):
     fecha_actual=datetime.datetime.now()
     return render(request, "camaras.html", {"dameFecha":fecha_actual})

def cansat(request):
     fecha_actual=datetime.datetime.now()
     return render(request, "cansat.html", {"dameFecha":fecha_actual})

def Eyeccion(request):
     fecha_actual=datetime.datetime.now()
     return render(request, "Eyeccion.html", {"dameFecha":fecha_actual})

def giroscopio(request):
     fecha_actual=datetime.datetime.now()
     return render(request, "giroscopio.html", {"dameFecha":fecha_actual})

def localizacion(request):
     fecha_actual=datetime.datetime.now()
     return render(request, "localizacion.html", {"dameFecha":fecha_actual})

def mision(request):
     fecha_actual=datetime.datetime.now()
     return render(request, "mision.html", {"dameFecha":fecha_actual})

def despedida(request):
    return HttpResponse("nos veremos.")


def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    juan="""<html>
    <body>
    <h3>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>"""% fecha_actual

    return HttpResponse(juan)
def calculaEdad(request,edad,agno):

   #edadActual=18
    periodo=agno-2019
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendás %s años </h1></body></html>" %(agno, edadFutura)

    return HttpResponse (documento) 