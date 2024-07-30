from django.db import models

class Articulo(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
