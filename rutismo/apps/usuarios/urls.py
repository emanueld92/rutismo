

from django.urls import path, include
from django.contrib.auth.decorators import login_required

from.views import Login, logoutUser, Inicio
app_name = "usuario"
urlpatterns = [
    path('',(Inicio.as_view()), name='index'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUser), name='logout'),
]
