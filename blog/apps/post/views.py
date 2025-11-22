from django.views.generic import ListView

class PostListView(ListView):
    template_name = 'post/post-list.html'
