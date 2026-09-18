from django.db import models


class Propietario(models.Model):
    identificacion = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.identificacion
