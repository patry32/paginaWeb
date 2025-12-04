from django.views.generic import TemplateView
from django.shortcuts import render

class PostListView(TemplateView):
    template_name = 'post/post-list.html'

def consejos_view(request):
    return render(request, 'post/consejos.html')

def contacto_view(request):
    return render(request, 'post/contacto.html')

def adopciones_view(request):
    return render(request, 'post/adopciones.html')

def mascotas(request):
    return render(request, "post/usuario-profile.html")


