from django.http import HttpResponse
from django.shortcuts import render
from appveterinaria.models import Alimentogato, Alimentopeces, Alimentoperro
from appveterinaria.forms import FormularioBusqueda, FormularioInsertarDatos

def index (request):

    lista= Alimentogato.objects.all ()

    if request.GET.get("producto"):
    
        formulario = FormularioBusqueda(request.GET)

        if formulario.is_valid():

            data= formulario.cleaned_data            
            lista= Alimentogato.objects.filter(marca__icontains = data ["producto"])
        
        return render ( request, "appveterinaria/hola.html",{"productos": lista,"formulario" : formulario})

    else:
        formulario = FormularioBusqueda()
        return render ( request, "appveterinaria/hola.html",{"productos": lista, "formulario" : formulario})

def indef (request):  

    listas= Alimentogato.objects.all ()
    return render ( request, "appveterinaria/perro.html",{"productos": listas})

def indes (request):  

    listas= Alimentoperro.objects.all ()
    return render ( request, "appveterinaria/perro.html",{"productos": listas})

def indez (request):  

    listass= Alimentopeces.objects.all ()
    return render ( request, "appveterinaria/peces.html",{"productos": listass})

def indea (request):  
    return render ( request, "appveterinaria/info.html")


def indei (request):

    if request.method == 'GET':
    
        formularios = FormularioInsertarDatos()

        return render ( request,"appveterinaria/busqueda.html",{"formularios" : formularios})

    else:
        formularios = FormularioInsertarDatos(request.POST)
       
        if formularios.is_valid():
            datas= formularios.cleaned_data  

            marca = datas.get ["marca"]
            alimento =   Alimentogato (marca=marca) 
            
            alimento.save ()

            return render (request, "appveterinaria/hola.html" )

        else:
            return  HttpResponse (f"La informacion ingresada no es correcta")


