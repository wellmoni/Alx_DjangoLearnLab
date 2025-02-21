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
from django.contrib.auth import login, logout, register
from django.contrib.auth.forms import UserCreationForm

class BookDetailView(DetailView):
      model = Book
      template_name = 'relationship_app/list_books.html'
      context_object_name = 'book'

##return render (request, 'relationship_app/library_detail.html', "library",)
class register(UserCreationForm):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.userprofile.role =='Admin'
def is_librarian(user):
    return user.userprofile.role =='librarian'
def is_member(user):
    return user.userprofile.role =='member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin.html', {'role': 'Admin'})

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html', {'role': 'librarian'})
@user_passes_test(is_admin)

def member_view(request):
    return render(request, 'relationship_app/member.html', {'role': 'member'})
# Create your views here.
