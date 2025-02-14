# Retrieve Book Entry
from bookshelf.models import Book

books = Book.objects.get(title = "1984")
for book in books:
    print(book.title, "-", book.author, "-", book.publication_year)
