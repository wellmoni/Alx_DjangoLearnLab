from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# User Registration
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")  
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

# User Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

# User Logout
def logout_view(request):
    logout(request)
    return redirect("login")

# Profile Management
@login_required
def profile_view(request):
    return render(request, "blog/profile.html", {"user": request.user})
from .models import Profile
from django.contrib.auth.forms import UserChangeForm

@login_required
def profile_view(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# List View - Display all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # Template file
    context_object_name = "posts"
    ordering = ["-published_date"]  # Show latest posts first

# Detail View - Display single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

# Create View - Allow authenticated users to create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to logged-in user
        return super().form_valid(form)

# Update View - Allow only the author to edit their post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only author can edit

# Delete View - Allow only the author to delete their post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only author can delete



# Create your views here.
