from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from apps.post.forms import PostCreateForm
from apps.post.models import Post, PostImage
from django.urls import reverse, reverse_lazy
from django.conf import settings

class PostCreateView(CreateView):
    template_name = 'post/post-create.html'
    form_class = PostCreateForm
    model = Post

    def get_success_url(self):
        return reverse('post:post-detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save()

        images = self.request.FILES.getlist('images')
        if images:
            for image in images:
                PostImage.objects.create(post=post, image=image)
        else:
            PostImage.objects.create(
                post=post, image=settings.POST_DEFAULT_IMAGE)
        return super().form_valid(form)


class PostListView(TemplateView):
    template_name = 'post/post-list.html'
    pass

class PostDetailView():
    template_name = 'post/post-detail.html'
    pass

class PostUpdateView():
    template_name = 'post/post-update.html'
    pass

class PostDeleteView():
    template_name = 'post/post-delete.html'
    pass

class CommentCreateView():
    template_name = 'post/post-comment.html'
    pass

class CommentUpdateView():
    template_name = 'post/post-update.html'
    pass

class CommentDeleteView():
    template_name = 'post/post-update.html'
    pass

def consejos_view(request):
    return render(request, 'post/consejos.html')

def contacto_view(request):
    return render(request, 'post/contacto.html')

def adopciones_view(request):
    return render(request, 'post/adopciones.html')

def mascotas(request):
    return render(request, "post/usuario-profile.html")


