from django.shortcuts import render
from .models import clientes, quem_somos, inicio, portfolio, serviços
from .forms import Contato

def home(request):
    cliente = clientes.objects.all()
    quemSomos = quem_somos.objects.all()
    inic = inicio.objects.all()
    port = portfolio.objects.all()
    serv = serviços.objects.all()
    if request.method == 'POST':
        form = Contato(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()
            form = Contato()
    else:
        form = Contato()
    context = {
        'cliente': cliente,
        'quemSomos': quemSomos,
        'inic': inic,
        'port' : port,
        'serv' : serv,
        'form': form,
    }
    return render(request, 'index.html', context)

