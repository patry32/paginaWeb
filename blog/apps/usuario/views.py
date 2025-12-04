from django.views.generic import TemplateView
from django.shortcuts import render

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
    return render(request, 'usuario/aves.html')

def cachorros_view(request):
    return render(request, 'usuario/cachorros.html')

def adultos_view(request):
    return render(request, 'usuario/adultos.html')
def adultos_view(request):
    return render(request, 'usuario/aves.html')


