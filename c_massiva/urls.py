from django.urls import path
from .views import *

urlpatterns = [
    path('cmassiva/dashboard', cmassiva_index , name='cmassiva_dashboard'),
    path('logout', logoutUser, name='logout')
]