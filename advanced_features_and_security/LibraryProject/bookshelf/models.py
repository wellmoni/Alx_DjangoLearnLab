from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()


class CustomUserManager(BaseUserManager):
    create_user = models.CharField(max_length=100)
    create_superuser = models.CharField(max_length= 200)


class Meta:
        permissions = [
            ("can_view", "Can view documents"),
            ("can_create", "Can create documents"),
            ("can_edit", "Can edit documents"),
            ("can_delete", "Can delete documents"),
        ]
# Create your models here.
