from django import forms

from Negocio.models import TipoCuenta
from .models import Cuenta

class SolicitudCuentaForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=[(tipo.tipo_cuen, tipo.tipo_cuen) for tipo in TipoCuenta.objects.all()])

    class Meta:
        model = Cuenta
        fields = ['tipo']   