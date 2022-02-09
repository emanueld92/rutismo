from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields import AutoField

from django.forms.widgets import Select
from .models import Nino
from django.forms import ModelForm


class EligeForm(forms.Form):
    fecha = forms.DateField()
    nombre = forms.CharField()
    e_animo = forms.ChoiceField(widget=forms.Select)
    tipo = forms.CharField()


class NinoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.pop('adulto')
    class Meta:
        model = Nino
        fields = '__all__'
