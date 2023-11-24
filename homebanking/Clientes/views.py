from django.shortcuts import render
from django.views import View

from Clientes.models import Cliente

# Create your views here.

class DatosCliente(View):
    def get(self, request, customer_id):  
        cliente = Cliente.objects.get(pk=customer_id)      
        return render(request, "Clientes/datosCliente.html", {"cliente": cliente})