from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import uuid
import os

def get_avatar_filename(instance, filename):
    #nombre del UUID del usuario
    _, file_extension = os.path.splitext(filename)

    new_filename = f"user-{instance.id}-avatar{file_extension}"
    return os.path.join("user/avatar/", new_filename)

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    alias = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(
        upload_to=get_avatar_filename, default=settings.AVATAR_DEFAULT_IMAGE
    )

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        
    @property
    def is_registered(self):
        return self.groups.filter(name="registered").exists

    @property
    def is_collaborator(self):
        return self.groups.filter(name="collaborator").exists

    @property
    def is_moderator(self):
        return self.groups.filter(name="moderator").exists