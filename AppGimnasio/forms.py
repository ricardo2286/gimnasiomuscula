from django import forms

class Musculacionformulario(forms.Form):
  nombre = forms.CharField()
  apellido = forms.CharField()
  fecha_ingreso = forms.DateField()