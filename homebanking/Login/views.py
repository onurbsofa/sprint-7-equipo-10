from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.

class RegisterView(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,'register.html',{'form':form})
    
    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
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
            user=form.get_user()
            login(request,user)
            return redirect('home')
        return render(request,'login.html',{'form':form})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class HomeView(TemplateView):
    template_name='home.html'
