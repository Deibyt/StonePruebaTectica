from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre
