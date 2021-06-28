from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request): #Primera vista
    doc_externo = open("Proyecto_Prueba/platillas/plantillasaludo.html") #se abre un doc htmll ext se puede poner toda la ruta o cortada como se muestra

    p1 = Persona("Dulce", "Carolina")
    nombre = "Dulce"
    hora_actual = datetime.datetime.now()
    plt = Template(doc_externo.read())  #Se crea la plantilla del documento externo
    doc_externo.close() # se cierra el doc externo
    ctx = Context({"nombre_persona": nombre, "momento_actual": hora_actual, "nombre_clase": p1.nombre, "apellido_clase": p1.apellido}) # se crea el contexto

    documento = plt.render(ctx) # se renderiza el documento
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Adios, que le vaya bien")

def damefecha(request):
    fechaactual = datetime.datetime.now()
    documento = f"<html><body><h1>Esta es la fecha {fechaactual} con django</h1></body></html>"
    return HttpResponse(documento)

def calculaedad(request,anio): #recibe el parametro
    edadactual = 18
    periodo = anio - 2021
    edadfutura = edadactual +periodo
    documento = f'<html><body><h4>En el año {anio} tendrás {edadfutura} años</h4></body></html>'

    return HttpResponse(documento)
