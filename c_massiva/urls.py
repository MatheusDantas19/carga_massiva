from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    path('c_massiva/dashboard', cmassiva_index , name='cmassiva_dashboard'),
    path('logout', logoutUser, name='logout'),
    path('c_massiva/geradorcarga', cmassiva_gerarcarga, name='cmassiva_gerarcarga'),
    path('c_massiva/response', cmassiva_response, name='cmassiva_response'),
    path('c_massiva/opcoes', cmassiva_opcoes, name='cmassiva_opcoes')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)