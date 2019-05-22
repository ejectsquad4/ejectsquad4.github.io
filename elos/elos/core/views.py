from django.shortcuts import render
from .models import clientes, quem_somos, inicio, portfolio, serviços
from .forms import Contato

def home(request):
    cliente = clientes.objects.all()
    quemSomos = quem_somos.objects.all()
    inic = inicio.objects.all()
    port = portfolio.objects.all()
    serv = serviços.objects.all()
    context_dict={}
    if request.method == 'POST':
        form = Contato(request.POST)
        if form.is_valid():
            context_dict['is_valid'] = True
            form.send_mail()
            form = Contato()
    else:
        form = Contato()
    
    context_dict['cliente'] = cliente
    context_dict['quemSomos'] = quemSomos
    context_dict['inic'] = inic
    context_dict['port'] = port
    context_dict['serv'] = serv
    context_dict['form'] = form
    
    return render(request, 'index.html', context_dict)

