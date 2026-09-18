from django.db import models

# Create your models here.
class Propietario(models.Model):
    identificacion = models.TextField(max_length=15)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.TextField(max_length=100)

    def __srt__(self):
        return self.identificacion