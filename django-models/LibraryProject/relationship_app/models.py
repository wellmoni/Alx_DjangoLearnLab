from django.db import models
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')

    
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books =  models.ManyToManyField(Book, related_name='book')

    def __str__(self):
        return self.title

Role_choices = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]  

class UserProfile(models.Model):
    user = models.OneToOneField ( on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=Role_choices, default='Member')



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)




class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE )
# Create your models here.
