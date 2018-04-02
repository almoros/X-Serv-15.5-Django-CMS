from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages
# Create your views here.

def pagina_inicial(request):
    respuesta = "Esto es la página inicial,"
    respuesta += " y estos son los recursos que hay:"
    lista = Pages.objects.all()
    for pagina in lista:
        respuesta += '<br><a href="/web/' + str(pagina.id) + '">' + pagina.name + '</a>'

    return HttpResponse(respuesta)

def pagina(request,identificador):
    try:
        pagina = Pages.objects.get(id = identificador)
        respuesta = "Has introducido " + str(pagina.id) + " que corresponde a: " + str(pagina.page) + " y su id es: " + str(pagina.id)
    except Pages.DoesNotExist:
        respuesta = "No existe la pagina con el identificador " + str(identificador)

    return HttpResponse(respuesta)
