from django.db import models
from Propietario.models import Propietario


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    propietario = models.ForeignKey(
        Propietario,
        on_delete=models.CASCADE,
        related_name='mascotas'
    )

    def __str__(self):
        return self.nombre
