from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar', cadastrarUsuario, name='cadastro'),
    path('login', loginUsuario, name='login'),
    path('', index, name='index')
]