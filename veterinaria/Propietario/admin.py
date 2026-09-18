from django.contrib import admin

from .models import Propietario


@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'telefono', 'email')
