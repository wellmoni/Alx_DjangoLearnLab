from django.contrib import admin
from django.urls import path
from . import views
from .views import BookDetailView 
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import RegisterView
from django.urls import path

##urlpatterns = [

    ##path('book_list/', views.list_books, name='book'),
   ## path('BookDetailView/', views.BookDetailView.as_view(), name='book_detail'),
    ##path('admin/', admin.site.urls),
##]


urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration_app/logout.html'), name='logout')
    path('register/', RegisterView.as_view(template_name='registration_app/register.html'), name='register')
]