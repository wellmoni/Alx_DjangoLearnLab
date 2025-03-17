from django.urls import path
from .views import register_view, login_view, logout_view, profile_view

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
]

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
from django.urls import path
from . import views

from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
