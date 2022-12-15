from django import forms
from ejemplo.models import Familiar, Mascota, Vehiculo


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget= forms.TextInput(attrs ={'placeholder': 'Busque algo...'}))

class Buscar_Mascota(forms.Form):
    nombre_mascota = forms.CharField(max_length=100,
                            widget= forms.TextInput(attrs ={'placeholder': '...'}))

class Buscar_Vehiculo(forms.Form):
    titular = forms.CharField(max_length=100,
                            widget= forms.TextInput(attrs ={'placeholder': '...'}))


class FamiliarForm(forms.ModelForm):
  class Meta: 
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
  class Meta: 
    model = Mascota
    fields = ['animal', 'nombre', 'dueno']

class VehiculoForm(forms.ModelForm):
  class Meta: 
    model = Vehiculo
    fields = ['tipo', 'marca', 'titular']

