from django.urls import path
import apps.post.views as Views
from . import views

app_name = "post"

urlpatterns = [
    path('posts/', Views.PostListView.as_view(), name="post-list"),
    path('consejos/', views.consejos_view, name='consejos'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('adopciones/', views.adopciones_view, name='adopciones'),
    path('mascotas/', views.mascotas, name='mascotas'),
]