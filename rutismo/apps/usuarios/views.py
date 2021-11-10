from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
# Vista generica basaad en clases para usos de formularios
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from .forms import formularioLogin
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, View
from ..ruta.views import Dasboard

# Create your views here.


class Inicio(TemplateView):
    template_name = 'index.html'


class Login(FormView):
    template_name = 'login2.html'
    form_class = formularioLogin
    success_url = reverse_lazy('ruta:dasboard')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
