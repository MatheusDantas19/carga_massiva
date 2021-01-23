from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listarUsuario, name='listar_usuario'),
    path('cadastrar', inserirUsuario, name='cadastrar_usuario'),
    path('login', login, name='login')
]