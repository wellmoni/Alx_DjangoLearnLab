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


class BookDetailView(DetailView):
      model = Book
      template_name = 'relationship_app/list_books.html'
      context_object_name = 'book'

##return render (request, 'relationship_app/library_detail.html', "library",)



# Create your views here.
