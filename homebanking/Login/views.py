from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from Login.models import UserProfile
from Clientes.models import Cliente
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from rest_framework import status

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterUserSerializer
from django.contrib.auth.models import User

class LoginAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(View):
    def get(self,request):
        form=CustomUserCreationForm()
        return render(request,'register.html',{'form':form})
    
    def post(self,request):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            cliente = Cliente.objects.get(customer_id=form.cleaned_data.get('customer_id'))
            user=form.save()  # Make sure to save the User before creating the UserProfile            
            UserProfile.objects.create(user=user, customer=cliente)
            login(request,user)
            return redirect('home')
        return render(request,'register.html',{'form':form})

class LoginView(View):
    def get(self,request):
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request):
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request,'login.html',{'form':form})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class HomeView(TemplateView):
    template_name='home.html'

