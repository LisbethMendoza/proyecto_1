
from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Nombre de usuario único
    password = models.CharField(max_length=128)  # Contraseña

    def __str__(self):
        return self.username
