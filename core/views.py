# entende HTML
from django.shortcuts import render, HttpResponse

# view linkada em urls para mostrar
# Create your views here.
def inicio(request, nome):
    return HttpResponse(f'<h1>Hi {nome}</h1>')
