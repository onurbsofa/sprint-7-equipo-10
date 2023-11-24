from django.shortcuts import render
from django.views import View

from Clientes.models import Cliente
from Login.models import UserProfile
from .models import Cuenta

# Create your views here.
class CuentasCliente(View):
    def get(self, request):
        profile = UserProfile.objects.get(user_id=request.user)
        customer_id = profile.customer_id
        cliente = Cliente.objects.get(pk=customer_id)   
        cuentas = Cuenta.objects.filter(customer_id=customer_id)
        return render(request, "cuentasDeCliente.html", {'cuentas': cuentas, 'cliente': cliente})