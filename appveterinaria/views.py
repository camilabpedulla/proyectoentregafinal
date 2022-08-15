from django.http import HttpResponse
from django.shortcuts import render
from appveterinaria.models import Alimentogato, Alimentopeces, Alimentoperro
from appveterinaria.forms import FormularioBusqueda, FormularioInsertarDatos,FormularioInsertarDatos_peces, FormularioInsertarDatos_perro

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


def insertardatosgatos (request):

    if request.method == 'GET':
    
        formularios = FormularioInsertarDatos()

        return render ( request,"appveterinaria/cargadatosgatos.html",{"formularios" : formularios})

    else:
        formularios = FormularioInsertarDatos(request.POST)
       
        if formularios.is_valid():

            data= formularios.cleaned_data  

            marca = data.get ("marca")
            producto =   Alimentogato (marca=marca) 
            
            producto.save ()

            return HttpResponse(f"La informacion fue ingresada correctamente")

        else:
            return  HttpResponse (f"La informacion ingresada no es correcta")


def insertardatosperro (request):

    if request.method == 'GET':
    
        formularios = FormularioInsertarDatos_perro()

        return render ( request,"appveterinaria/cargadatosperro.html",{"formularios" : formularios})

    else:
        formularios = FormularioInsertarDatos_perro(request.POST)
       
        if formularios.is_valid():

            data= formularios.cleaned_data  

            marca = data.get ("marca")
            producto =   Alimentoperro (marca=marca) 
            
            producto.save ()

            return HttpResponse(f"La informacion fue ingresada correctamente")

        else:
            return  HttpResponse (f"La informacion ingresada no es correcta")


def insertardatospeces (request):

    if request.method == 'GET':
    
        formularios = FormularioInsertarDatos_peces()

        return render ( request,"appveterinaria/cargadatospeces.html",{"formularios" : formularios})

    else:
        formularios = FormularioInsertarDatos_peces(request.POST)
       
        if formularios.is_valid():

            data= formularios.cleaned_data  

            marca = data.get ("marca")
            producto =   Alimentopeces (marca=marca) 
            
            producto.save ()

            return HttpResponse(f"La informacion fue ingresada correctamente")

        else:
            return  HttpResponse (f"La informacion ingresada no es correcta")
