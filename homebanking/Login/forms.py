from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    customer_id = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('customer_id',)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
    widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')