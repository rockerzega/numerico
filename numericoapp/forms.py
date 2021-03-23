from django import forms

class CamposDinamicos(forms.Form):
    prueba = forms.IntegerField(initial=2,min_value=2, label="Aqui su numero")
    datos = forms.CharField(label="Aqui su texto")

class SplineForm (forms.Form):
    x = forms.FloatField(
        initial=0.0,
        required=False,
    )
    y = forms.FloatField(
        required=False,
        initial=0.0
    )
    dydx = forms.FloatField(
        required=False,
        initial=0.0
    )

