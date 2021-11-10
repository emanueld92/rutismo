from django.forms import fields
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from apps.ruta.models import Bitacora
# Create your views here.


class Dasboard(TemplateView):

    template_name = "home.html"
   


class Elige(CreateView):
    model=Bitacora
    fields=['nombre_bitacora','e_animo','tipo']
    success_url = reverse_lazy('ruta:dasboard')
    def post(self, request, *args, **kwargs):
        
        print ("Estos son los argumentos",self.args, " Estos los los kgwar")
        return super().post(request, *args, **kwargs)
    
    
    
class Comenzar(TemplateView):
    template_name = "comenzar.html"


class Estado(TemplateView):
    template_name = "estado.html"


class Horarios(TemplateView):
    template_name = "horarios.html"


class Ayuda(TemplateView):
    template_name = "help.html"
