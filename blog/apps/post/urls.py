from django.urls import path
import apps.post.views as Views

app_name = "post"

urlpatterns = [
    path('posts/', Views.PostListView.as_view(), name="post-list"),
]