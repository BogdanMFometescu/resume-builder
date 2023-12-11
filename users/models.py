from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True, null=True)
    username = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    bio = models.CharField(max_length=500,blank=True,null=True)
    profile_image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.username
