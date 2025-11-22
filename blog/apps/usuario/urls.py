from django.urls import path
import apps.usuario.views as Views

app_name = "usuario"

urlpatterns = [
    path('usuario/profile', Views.UserProfileView.as_view(), name="user-profile"),
]