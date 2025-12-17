from django.urls import path
import apps.post.views as views
from . import views

app_name = "post"

urlpatterns = [
    #crear post
    path('posts/', views.PostListView.as_view(), name="post-list"),
    path('posts/create', views.PostCreateView.as_view(), name="post-create"),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name="post-detail"),
    path('posts/<slug:slug>/update', views.PostUpdateView.as_view(), name="post-update"),
    path('posts/<slug:slug>/delete', views.PostDeleteView.as_view(), name="post-delete"),

    #comentarios
    path('posts/<slug:slug>/comment/create', views.CommentCreateView.as_view(), name="comment-create"),
    path('comments/<uuid:pk>/update', views.CommentUpdateView.as_view(), name="comment-update"),
    path('comments/<uuid:pk>/delete', views.CommentDeleteView.as_view(), name="comment-delete"),

    #Categorias
    path('consejos/', views.consejos_view, name='consejos'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('adopciones/', views.adopciones_view, name='adopciones'),
    path('mascotas/', views.mascotas, name='mascotas'),
]