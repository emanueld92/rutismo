from django import forms
from django.db.models.fields import AutoField
from django.forms.widgets import Select

class EligeForm(forms.Form):
    fecha=forms.DateField()
    nombre=forms.CharField()
    e_animo=forms.ChoiceField(widget=forms.Select)
    tipo=forms.CharField()
    
    