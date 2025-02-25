from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import create_user 
from .models import create_superuser

admin.site.register(create_user, create_superuser)


# Register your models here.
