from logging import PlaceHolder
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
        labels = {
            'nombre': 'Nombre',
            'f_nacimiento': "Fecha de Nacimiento",
            'genero': 'Genero',
            'foto': 'Foto',
        }
        widgets = {  # los Widgets te permiten darle estilo a nuestros imput y attrs son los atributos de imput
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',

                    'id': 'nombre',
                }
            ),

            'f_nacimiento': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',

                    'id': 'f_nacimiento',
                }
            ),
            'genero': forms.Select(
                attrs={
                    'class': 'form-control',

                    'id': 'genero',
                }
            ),
            'foto': forms.FileInput(  # FileInput es para subir archivos
                attrs={
                    'type': 'file',
                    'class': 'form-control',
                    'id': 'foto', }),
        }
        # widget={
        #     'nombre':forms.TextInput(attrs={'class':'form-control'}),
        #     'f_nacimiento':forms.SelectDateWidget(attrs={'class':'form-control'}),
        #     'genero':forms.RadioSelect(attrs={'class':'form-control'}),
        #     'foto':forms.FileInput(attrs={'class':'form-control'}),
        # }
