from django.contrib import admin

from .models import Categoria, Marca, Modelo, Cor, Acessorio, Veiculo

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Cor)
admin.site.register(Acessorio)
admin.site.register(Veiculo)


# Register your models here.
