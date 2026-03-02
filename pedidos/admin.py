from django.contrib import admin

# Criando o admin para os modelos de pizza , sabores e acompanhamentos
from . models import Pizza, Sabores, Acompanhamentos

admin.site.register(Pizza)
admin.site.register(Sabores)
admin.site.register(Acompanhamentos)