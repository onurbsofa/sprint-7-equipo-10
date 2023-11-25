from django.shortcuts import render
from django.views import View

from Clientes.models import Cliente
from Login.models import UserProfile
from .models import Cuenta
from .forms import SolicitudCuentaForm
import random
import string

# Create your views here.
class CuentasCliente(View):
    def get(self, request):
        profile = UserProfile.objects.get(user_id=request.user)
        customer_id = profile.customer_id
        cliente = Cliente.objects.get(pk=customer_id)   
        cuentas = Cuenta.objects.filter(customer_id=customer_id)
        return render(request, "cuentasCliente.html", {'cuentas': cuentas, 'cliente': cliente})
    
class SolicitarCuenta(View):
    def get(self, request):
        form = SolicitudCuentaForm()
        return render(request, "solicitudCuenta.html", {'form': form})
    
    def post(self, request):
        form = SolicitudCuentaForm(request.POST)

        def generate_iban(country_code='ES'):
            control_digits = ''.join(random.choices(string.digits, k=2))
            account_number = ''.join(random.choices(string.digits, k=20))
            iban = country_code + control_digits + account_number
            return iban

        if form.is_valid():
            customer_id = Cliente.objects.get(customer_id=request.user.userprofile.customer_id)
            balance = 0
            iban = generate_iban()
            tipo = form.cleaned_data.get('tipo')
            Cuenta.objects.create(customer_id=customer_id, balance=balance, iban=iban, tipo=tipo)
        else:
            print(form.errors)
        return render(request, "solicitudCuenta.html", {'form': form})