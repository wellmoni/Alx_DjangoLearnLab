from django.shortcuts import render

def list_books(request):
    books = Book.objects.all()
    
   ## book_info = "\n".join([f"{book.title} by {book.author}" for book in books])
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from .models import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView, RegisterView
from django.urls import path 


class BookDetailView(DetailView):
      model = Book
      template_name = 'relationship_app/list_books.html'
      context_object_name = 'book'

##return render (request, 'relationship_app/library_detail.html', "library",)
urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(template_name='registration_app/register.html'),name='register')
]


# Create your views here.
