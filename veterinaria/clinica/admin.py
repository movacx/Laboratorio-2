from django.contrib import admin

from .models import ConsultaVeterinaria


@admin.register(ConsultaVeterinaria)
class ConsultaVeterinariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'fecha', 'motivo', 'costo')
