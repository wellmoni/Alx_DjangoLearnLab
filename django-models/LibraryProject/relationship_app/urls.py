from django.contrib import admin
from django.urls import path
from . import views
from .views import add_book, edit_book, delete_book
from .views import BookDetailView 
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import RegisterView
from .views import admin_view
from .views import librarian_view
from .views import member_view

from django.urls import path

##urlpatterns = [

    ##path('book_list/', views.list_books, name='book'),
   ## path('BookDetailView/', views.BookDetailView.as_view(), name='book_detail'),
    ##path('admin/', admin.site.urls),
##]


##urlpatterns = [
  ##  path('login/', LoginView.as_view(template_name='registration_app/login.html'), name='login'),
    ##path('logout/', LogoutView.as_view(template_name='registration_app/logout.html'), name='logout'),
    ##path('register/', views.register(template_name='registration_app/register.html'), name='register')
##]

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),

    path('add_book', add_book, name='add_book')
    path('edit_book',edit_book, name ='edit_book'),
]