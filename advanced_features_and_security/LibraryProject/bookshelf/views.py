from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .forms import ExampleForm

@permission_required('book_list', raise_exception= books)


# Create your views here.
