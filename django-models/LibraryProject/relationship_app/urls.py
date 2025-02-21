from django.contrib import admin
from django.urls import path
from . import views
from .views import BookDetailView 
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import RegisterView
from django.contrib.auth.views import admin_view
from django.contrib.auth.views import member_view
from django.contrib.auth.views import librarian_view

from django.urls import path

##urlpatterns = [

    ##path('book_list/', views.list_books, name='book'),
   ## path('BookDetailView/', views.BookDetailView.as_view(), name='book_detail'),
    ##path('admin/', admin.site.urls),
##]


urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration_app/logout.html'), name='logout'),
    path('register/', views.register(template_name='registration_app/register.html'), name='register')
]

urlpatterns = [
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
]