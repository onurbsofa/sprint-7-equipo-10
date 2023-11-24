from django.shortcuts import render
from django.views import View
from Login.models import UserProfile
from Clientes.models import Cliente

# Create your views here.

class DatosCliente(View):
    def get(self, request):
        profile = UserProfile.objects.get(user_id=request.user)
        customer_id = profile.customer_id
        cliente = Cliente.objects.get(pk=customer_id)      
        return render(request, "datosCliente.html", {"cliente": cliente})