from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
# Create your views here.


class Dasboard(TemplateView):

    template_name = "home.html"
   


class Elige(TemplateView):
    template_name="elige.html"
    
    
class Comenzar(TemplateView):
    template_name = "comenzar.html"


class Estado(TemplateView):
    template_name = "estado.html"


class Horarios(TemplateView):
    template_name = "horarios.html"


class Ayuda(TemplateView):
    template_name = "help.html"
