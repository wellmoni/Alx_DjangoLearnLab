from django.contrib import admin
from django.urls import path
from . import views
from .views import BookDetailView 
from .views import list_books

urlpatterns = [

    path('book_list/', views.list_books, name='book'),
    path('BookDetailView/', views.BookDetailView.as_view(), name='book_detail'),
    path('admin/', admin.site.urls),
]
