from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.userprofile.role =='Admin'
def is_librarian(user):
    return user.userprofile.role =='Librarian'
def is_member(user):
    return user.userprofile.role =='Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin.html', {'role': 'Admin'})

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html', {'role': 'Librarian'})
@user_passes_test(is_admin)

def member_view(request):
    return render(request, 'relationship_app/member.html', {'role': 'Member'})
# Create your views here.
