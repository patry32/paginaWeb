from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'bg-blue-50', 'placeholder': 'contraseña'}
    ))

    password = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'bg-blue-50', 'placeholder': 'contraseña'}
    
 ))