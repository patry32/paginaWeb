from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from django.contrib.auth.views import LoginView as LoginViewDjango, LogoutView as LogoutViewDjango
from django.contrib.auth.models import Group
from apps.usuario.forms import LoginForm, RegisterForm
from django.urls import reverse_lazy
import logging

def login_view(request):
    return render(request, 'usuario/login.html')

def registro_view(request):
    return render(request, 'registro.html')

def profile_view(request):
    return render(request, 'usuario/user-profile.html')

class UserProfileView(TemplateView):
    template_name = 'usuario/user-profile.html'

def gatos_view(request):
    return render(request, 'usuario/gatos.html')

def aves_view(request):
    return render(request, 'usuario/Aves.html')

def cachorros_view(request):
    return render(request, 'usuario/cachorros.html')

def adultos_view(request):
    return render(request, 'usuario/adultos.html')

def urgente_view(request):
    return render(request, 'usuario/urgente.html')

class LoginView(LoginViewDjango):
    template_name = 'auth/auth-login.html'
    autentication_form = LoginForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')

        if next_url:
            return next_url
        return reverse_lazy('home')
    
class RegisterView(CreateView):
    template_name = 'auth/auth-register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        registered_group = Group.objects.get(name="registered")
        self.object.groups.add(registered_group)

        return response
    
class LogoutView(LogoutViewDjango):
    def get_success_url(self):
        next_url = self.request.GET.get('next')

        if next_url:
            return next_url
        
        return reverse_lazy('home')