from django import forms
from apps.post.models import Post, PostImage, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'allow_comments']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'allow_comments': 'Permitir comentarios',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-pink-500',
                'placeholder': 'Escribí el título del post',
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 h-32 focus:outline-none focus:ring-2 focus:ring-pink-500',
                'placeholder': 'Escribí el contenido del post',
            }),
        }

class PostCreateForm(PostForm):
    image = forms.ImageField(
        required=False,
        label='Imagen',
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg p-2'
        })
    )

    def save(self, commit=True):
        post = super().save(commit=False)
        image = self.cleaned_data.get('image')

        if commit:
            post.save()
            if image:
                PostImage.objects.create(post=post, image=image)

        return post

class PostUpdateForm(PostForm):
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Agrega un comentario...',
                'class': 'w-full p-3 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']