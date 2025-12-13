from django.contrib import admin
from apps.post.models import Post, Category, PostImage

class PostAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'author', 'created_at',
                    'update_at', 'allow_comments')

    search_fields =('title', 'content', 
                    'author__username', 'author__id', 'id')
    prepopulated_fields ={'slug': ('title',)}
    list_filter =('created_at', 'allow_comments')
    ordering =('-created_at',)

class CategoryAdmin(admin.ModelAdmin):
    list_display =('id', 'title')

class PostImageAdmin(admin.ModelAdmin):
    list_display =('post', 'image', 'active',)
    search_fields =('post__title', 'post__id', 'image', 'id')
    list_filter =('active',)
    ordering =('-created_at',)

    def activate_images(self, recuest, queryset):
        update = queryset.update(activate=True)
        self.message_user(recuest, f"{update} imagenes fueron activadas correctamente")

    activate_images.short_description = "activar imagenes selecionadas"


    def desactivate_images(self, recuest, queryset):
        update = queryset.update(activate=False)
        self.message_user(recuest, f"{update} imagenes fueron desactivadas correctamente")

    desactivate_images.short_description = "desactivar imagenes selecionadas"

    actions = [activate_images,
               desactivate_images]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostImage, PostImageAdmin)