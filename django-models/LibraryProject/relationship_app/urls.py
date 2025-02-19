from django.contrib import admin
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView


urlpatterns = [

    path('book/', views.book_list, name='book'),
    path('detail/', views.BookDetailView(), name='detail'),
    path('admin/', admin.site.urls),
]
