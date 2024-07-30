from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
    
class Permiso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"

class UsuarioRol(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permisos = models.ManyToManyField(Permiso, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.rol.nombre}"
