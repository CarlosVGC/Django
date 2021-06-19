from django.http import HttpResponse

def saludo(request): #Primera vista
    return HttpResponse("Esta es la primera pagina con django")

def despedida(request):
    return HttpResponse("Adios, que le vaya bien")
