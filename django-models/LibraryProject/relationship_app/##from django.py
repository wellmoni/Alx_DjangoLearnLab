##from django.shortcuts import render

##def list_books(request):
    ##books = Book.objects.all()
    
   ## book_info = "\n".join([f"{book.title} by {book.author}" for book in books])
    ##return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from .models import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView, RegisterView
from django.urls import path 
from django.contrib.auth import login, logout, register
from django.contrib.auth.forms import UserCreationForm

##class BookDetailView(DetailView):
     ## model = Book
      ##template_name = 'relationship_app/list_books.html'
     ## context_object_name = 'book'

##return render (request, 'relationship_app/library_detail.html', "library",)
##class register(UserCreationForm):
   ## form_class = UserCreationForm()
    ##success_url = reverse_lazy('login')
    ##template_name = 'relationship_app/register.html'