from django.urls import path
from . import views

app_name = "usuario"

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    # Registro / login
    path('auth/login/', views.LoginView.as_view(), name="auth-login"),
    path('auth/register/', views.RegisterView.as_view(), name="auth-register"),
    path('auth/logout/', views.LogoutView.as_view(), name="auth-logout"),


    # Tus vistas extra
    path('gatos/', views.gatos_view, name='gatos'),
    path('aves/', views.aves_view, name='aves'),
    path('cachorros/', views.cachorros_view, name='cachorros'),
    path('adultos/', views.adultos_view, name='adultos'),
    path('urgente/', views.urgente_view, name='urgente'),
]
