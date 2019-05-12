from django.shortcuts import render
from django.http import HttpResponse
from .models import clientes

def home(request):
    cliente = clientes.objects.all()
    context = {
        'cliente': cliente
    }
    return render(request, 'index.html', context)

