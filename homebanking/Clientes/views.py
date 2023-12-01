from django.shortcuts import render
from django.views import View
from Login.models import UserProfile
from Clientes.models import Cliente
from rest_framework import viewsets
from .serializers import ClienteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class DatosCliente(View):
    def get(self, request):
        profile = UserProfile.objects.get(user_id=request.user)
        customer_id = profile.customer_id
        cliente = Cliente.objects.get(pk=customer_id)      
        return render(request, "datosCliente.html", {"cliente": cliente})


class DatosClienteList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        profile = UserProfile.objects.get(user_id=request.user)
        customer_id = profile.customer_id
        cliente = Cliente.objects.get(pk=customer_id) 
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)