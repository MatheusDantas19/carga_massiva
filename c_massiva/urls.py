from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    path('cmassiva/dashboard', cmassiva_index , name='cmassiva_dashboard'),
    path('logout', logoutUser, name='logout'),
    path('cmassiva/geradorcarga', cmassiva_gerarcarga, name='cmassiva_gerarcarga'),
    path('cmassiva/response', cmassiva_response, name='cmassiva_response'),
    path('cmassiva/opcoes', cmassiva_opcoes, name='cmassiva_opcoes')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)