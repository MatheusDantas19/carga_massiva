from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    bio = models.TextField(blank=True)


# Create your models here.

# class Usuario(models.Model):
#     nome = models.CharField(max_length=30, null=False, blank=False)
#     sobrenome = models.CharField(max_length=30, null=False, blank=False)
#     usuario = models.CharField(max_length=30, null=False, blank=False, unique=True)
#     senha = models.CharField(max_length=15, null=False, blank=False)

def __str__(self):
    return self.first_name
