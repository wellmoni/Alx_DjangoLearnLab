from django.contrib import admin
from django.urls import path
from . import views
from .views import BookDetailView 

urlpatterns = [

    path('book_list/', views.book_list, name='book'),
    path('BookDetailView/', views.BookDetailView.as_view(), name='book_detail'),
    path('admin/', admin.site.urls),
]
