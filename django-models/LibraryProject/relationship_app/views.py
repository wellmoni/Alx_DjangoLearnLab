from django.shortcuts import render

def book_list(request):
    books = books.objects.all()
    book_info = "\n".join([f"{book.title} by {book.author}" for book in books])
    return HttpResponse(f"<pre>{book_info}</pre>")

# Create your views here.
