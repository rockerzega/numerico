from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
from django.forms import ModelForm
from django import forms

class CamposDinamicos(forms.Form):
    prueba = forms.IntegerField(
        label='Aqui va el texto', 
        required=True, 
        initial=2, 
        min_value=2,
        )
    datos = forms.CharField(
        required=True,
    )
