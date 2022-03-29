
from re import template
from django.forms import fields
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View

from django.urls import reverse_lazy
from apps.ruta.models import Bitacora, Nino
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Nino
from .forms import NinoForm, EligeForm
# Create your views here.


class Dasboard(TemplateView):

    template_name = "home.html"


class Elige(CreateView):
    model = Bitacora
    fields = ['e_animo']
    success_url = reverse_lazy('ruta:dasboard')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CrearNino(CreateView):
    model = Nino
    form_class = NinoForm
    success_url = reverse_lazy('ruta:dasboard')
    template_name = 'ruta/nino_form.html'

    def form_valid(self, form):
        form.instance.adulto = self.request.user
        return super().form_valid(form)


class Comenzar(TemplateView):
    template_name = "comenzar.html"


class Estado(TemplateView):
    template_name = "estado.html"


class Horarios(TemplateView):
    template_name = "horarios.html"


class Ayuda(TemplateView):
    template_name = "help.html"


class ListadoNino(ListView):
    model = Nino
    success_url = reverse_lazy('ruta:dasboard')
    template_name = "nino_list.html"
    context_object_name = 'Ninos'
