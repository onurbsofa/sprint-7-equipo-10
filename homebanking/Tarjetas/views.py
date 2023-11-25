
from datetime import datetime, timedelta
from django.shortcuts import render
from django.views import View

from Login.models import UserProfile
from Tarjetas.models import Tarjeta
from Tarjetas.forms import SolicitudTarjetaForm
from Clientes.models import Cliente

import random

# Create your views here.

class TarjetasCliente(View):
    def get(self, request):
        profile = UserProfile.objects.get(user_id=request.user)
        customer_id = profile.customer_id 
        tarjetas = Tarjeta.objects.filter(customer_id=customer_id)
        return render(request, "tarjetasCliente.html", {'tarjetas': tarjetas})
    
class SolicitarTarjeta(View):
    def get(self, request):
        form = SolicitudTarjetaForm()
        return render(request, "solicitudTarjeta.html", {'form': form})
    
    def post(self, request):
        form = SolicitudTarjetaForm(request.POST)
        if form.is_valid():
            numero = random.randint(1000000000000000, 9999999999999999)
            while Tarjeta.objects.filter(numero=numero).exists():
                numero = random.randint(1000000000000000, 9999999999999999)
            tipo = form.cleaned_data.get('tipo')
            marca = form.cleaned_data.get('marca')
            cvv = random.randint(100, 999)
            customer_id = Cliente.objects.get(customer_id=request.user.userprofile.customer_id)
            fechaotorgamiento = datetime.now().date().strftime('%Y-%m-%d')
            fechaexpiracion = (datetime.now().date() + timedelta(days=1800)).strftime('%Y-%m-%d')
            Tarjeta.objects.create(numero=numero, cvv=cvv, tipo=tipo, marca=marca, fechaotorgamiento=fechaotorgamiento, fechaexpiracion=fechaexpiracion, customer_id=customer_id)
            return render(request, "solicitudTarjeta.html", {'form': form})
        else:
            print(form.errors)
            return render(request, "solicitudTarjeta.html", {'form': form})