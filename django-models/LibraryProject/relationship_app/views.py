from django.shortcuts import render

def book_list(request):
    books = Book.objects.all()
    
   ## book_info = "\n".join([f"{book.title} by {book.author}" for book in books])
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
      model = Book
      template_name = 'books/book_detail.html'



# Create your views here.
