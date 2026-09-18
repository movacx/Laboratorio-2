from django.db import models

# Create your models here.
class ConsultaVeterinaria(models.Model):
    mascota = models.CharField(max_length=100)
    fecha = models.DateField()
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __srt__(self):
        return self.mascota



# dentificacion, nombre,
# telefono, email 