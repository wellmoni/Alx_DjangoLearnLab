from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

# Create your models here.
