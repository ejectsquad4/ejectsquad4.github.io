from django.shortcuts import render
from .models import clientes, quem_somos, inicio

def home(request):
    cliente = clientes.objects.all()
    quemSomos = quem_somos.objects.all()
    inic = inicio.objects.all()
    context = {
        'cliente': cliente,
        'quemSomos': quemSomos,
        'inic': inic
    }
    return render(request, 'index.html', context)

