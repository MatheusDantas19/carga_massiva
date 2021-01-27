from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listarUsuario, name='listar_usuario'),
    path('cadastrar', cadastrarUsuario, name='cadastro'),
    path('login', loginUsuario, name='login'),
    path('logout', logoutUsuario, name='logout'),
    path('', index, name='index')
]