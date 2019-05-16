from django.contrib import admin
from .models import inicio, quem_somos, clientes, portfolio, serviços

admin.site.register(quem_somos)
admin.site.register(inicio)
admin.site.register(clientes)
admin.site.register(portfolio)
admin.site.register(serviços)