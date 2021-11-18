from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields import AutoField
from django.forms.models import model_to_dict
from django.forms.widgets import Select
from .models import Nino
from django.forms import ModelForm
    


class EligeForm(forms.Form):
    fecha = forms.DateField()
    nombre = forms.CharField()
    e_animo = forms.ChoiceField(widget=forms.Select)
    tipo = forms.CharField()


class NinoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields.pop('password')
        # self.fields.pop('is_staff')
        # self.fields.pop('last_login')
        # self.fields.pop('date_joined')
        # self.fields.pop('groups')
        # self.fields.pop('is_active')
        # self.fields.pop('user_permissions')
        # self.fields.pop('is_superuser')
        
    class Meta:
        model = Nino

        
        fields = ('nombre',
              'f_nacimiento',
              'genero',
              'foto',
              )
        labels = {  # Esto nos permite renderisar los label con codigo python y no html
        'nombre': 'Nombre',
        'f_nacimiento': 'Fecha de Nacimiento',
        'genero': 'Genero',
        'foto': 'Foto',

        }
        widgets = {  # los Widgets te permiten darle estilo a nuestros imput y attrs son los atributos de imput
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Su nombre',
                    'id': 'nombre',
                }
            ),
            'f_nacimiento': forms.SelectDateWidget(
                attrs={
                    'class':'form-control',
                    'id':'f_nacimiento',
                }
                
            ),
            'genero':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'genero'
                }
            ),
            'foto':forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'foto'
                }
            ),
            }
