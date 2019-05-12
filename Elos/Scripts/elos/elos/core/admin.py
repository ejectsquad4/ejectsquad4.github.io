from django.contrib import admin
from .models import inicio
from .models import quem_somos
from .models import clientes
from .models import portfolio

admin.site.register(quem_somos)
admin.site.register(inicio)
admin.site.register(clientes)
admin.site.register(portfolio)