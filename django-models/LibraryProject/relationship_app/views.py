from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

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


def is_admin(user):
    return user.userprofile.role =='Admin'
def is_librarian(user):
    return user.userprofile.role =='Librarian'
def is_member(user):
    return user.userprofile.role =='Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})
@user_passes_test(is_admin)

def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})


@permission_required('relationship_app.can_add_book', login_url='/login/')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to Edit a Book
@permission_required('relationship_app.can_change_book', login_url='/login/')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# View to Delete a Book
@permission_required('relationship_app.can_delete_book', login_url='/login/')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# Create your views here.
