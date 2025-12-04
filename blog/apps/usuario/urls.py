from django.urls import path, include
import apps.usuario.views as Views
from django.shortcuts import render
from . import views
from .views import UserProfileView

app_name = "usuario"

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('gatos/', views.gatos_view, name='gatos'),
    path('aves/', views.aves_view, name='aves'),
    path('cachorros/', views.cachorros_view, name='cachorros'),
    path('adultos/', views.adultos_view, name='adultos'),
    path('urgente/', views.adultos_view, name='urgente'),
]