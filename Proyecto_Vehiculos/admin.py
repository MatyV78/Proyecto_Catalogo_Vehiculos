from django.contrib import admin
from .models import Vehiculo, Marca, Cliente  # importa tus modelos

# Regístralos en el admin
admin.site.register(Vehiculo)
admin.site.register(Marca)
admin.site.register(Cliente)

