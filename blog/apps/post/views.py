from django.views.generic import TemplateView, CreateView, DeleteView, DetailView, UpdateView
from django.shortcuts import render
from apps.post.forms import PostCreateForm
from apps.post.models import Comment, Post, PostImage
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Comment
from .forms import CommentForm

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

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post/post-update.html'
    fields = ['title', 'content', 'image']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse('post:post-detail', kwargs={'slug': self.object.slug})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post/post-delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'post/post-comment.html'
    fields = ['content'] 
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post:post-detail', kwargs={'pk': self.kwargs['post_id']})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'post/post-comment.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.object.post.slug})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'post/post-comment-delete.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.object.post.slug})

def consejos_view(request):
    return render(request, 'post/consejos.html')

def contacto_view(request):
    return render(request, 'post/contacto.html')

def adopciones_view(request):
    return render(request, 'post/adopciones.html')

def mascotas(request):
    return render(request, "post/usuario-profile.html")


