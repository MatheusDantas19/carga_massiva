from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    sobrenome = models.CharField(max_length=30, null=False, blank=False)
    usuario = models.CharField(max_length=30, null=False, blank=False, unique=True)
    senha = models.CharField(max_length=15, null=False, blank=False)

def __str__(self):
    return self.first_name
