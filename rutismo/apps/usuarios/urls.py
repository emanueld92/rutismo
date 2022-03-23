

from django.urls import path, include
from django.contrib.auth.decorators import login_required

from.views import Login, Logout, Inicio,CustomerUserCreateView
app_name = "usuario"
urlpatterns = [
    path('',(Inicio.as_view()), name='index'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(Logout.as_view()), name='logout'),
    path('register/',CustomerUserCreateView.as_view(), name='register'),
]
