from django.db import models
from Mascota.models import Mascota


class ConsultaVeterinaria(models.Model):
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    fecha = models.DateField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100, blank=True)
    tratamiento = models.CharField(max_length=100, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Consulta de {self.mascota}'
