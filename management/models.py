from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models.base import BaseEntity


class User(AbstractUser):
    phone_number = models.IntegerField(default=0)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Profile(BaseEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    address = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.user.phone_number

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
