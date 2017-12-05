from django.shortcuts import render

def index(request):
    context={}
    return render(request,"index.html",context)

def about(request):
    context={}
    return render(request,"about.html",context)

def contact(request):
    context={}
    return render(request,"contact.html",context)

def marcos(request):
    context={}
    return render(request,"marcos.html",context)

def cajas(request):
    context={}
    return render(request,"cajas.html",context)    

def restauracion(request):
    context={}
    return render(request,"recuperacion.html",context)

def litografias(request):
    context={}
    return render(request,"litografias.html",context)

def galeria(request):
    context={}
    return render(request,"galeria.html",context)

def opciones(request):
    context={}
    return render(request,"opciones.html",context)