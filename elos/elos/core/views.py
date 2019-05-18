from django.shortcuts import render
from .models import clientes, quem_somos, inicio, portfolio, serviços

def home(request):
    cliente = clientes.objects.all()
    quemSomos = quem_somos.objects.all()
    inic = inicio.objects.all()
    port = portfolio.objects.all()
    serv = serviços.objects.all()
    context = {
        'cliente': cliente,
        'quemSomos': quemSomos,
        'inic': inic,
        'port' : port,
        'serv' : serv,
    }
    return render(request, 'index.html', context)

