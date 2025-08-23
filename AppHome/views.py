from django.shortcuts import render

# Create your views here.


def showInicio(request):
    return render(request, "index.html")


def showPresentacion(request):
    return render(request, "presentacion.html")


def showCatalogo(request):
    return render(request, "catalogo.html")