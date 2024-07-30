from django.db import models

class Transaccion(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    es_ingreso = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.descripcion} - {'Ingreso' if self.es_ingreso else 'Egreso'}"
