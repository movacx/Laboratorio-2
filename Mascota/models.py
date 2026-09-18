from django.db import models

# Create your models here.


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField()
    propietario = models.IntegerField()

    def __srt__(self):
        return self.nombre