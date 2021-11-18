
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.staticfiles.urls import static
from.views import *
app_name = "ruta"

urlpatterns = [
    path('dasboard/', login_required(Dasboard.as_view()), name='dasboard'),
    path('comenzar/', login_required(Comenzar.as_view()), name='comenzar'),
    path('elige/', login_required(Elige.as_view()), name='elige'),
    path('estado/', login_required(Estado.as_view()), name='estado'),
    path('horarios/', login_required(Horarios.as_view()), name='horarios'),
    path('Ayuda/', login_required(Ayuda.as_view()), name='ayuda'),
    
    
    path('registro_nino/', login_required(CrearNino.as_view()), name='crear_nino'),
]

