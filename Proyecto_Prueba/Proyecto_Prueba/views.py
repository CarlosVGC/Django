from django.http import HttpResponse
import datetime

def saludo(request): #Primera vista
    documento = "<html><body><h1>Esta es la primera pagina con django</h1></body></html>"
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
