from django import forms

from Negocio.models import Marcatarjeta
from .models import Tarjeta

class SolicitudTarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['tipo', 'marca']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['marca'].choices = [
            (marca.marca, marca.marca.capitalize) for marca in Marcatarjeta.objects.all()
        ]