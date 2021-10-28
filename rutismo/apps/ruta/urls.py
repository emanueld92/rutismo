
from django.urls import path
from django.contrib.auth.decorators import login_required

from.views import *

urlpatterns = [
    path('', login_required(Home.as_view()), name='home'),
    path('comenzar/', login_required(Comenzar.as_view()), name='comenzars'),
    path('elige/', login_required(Estado), name='elige'),
    path('estado/', login_required(Estado), name='estado'),
    path('horarios/', login_required(Horarios), name='horarios'),
    path('Ayuda/', login_required(Ayuda), name='ayuda'),
]
