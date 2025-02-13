 book = Book.objects.create(title = "1984", author = "George Orwell", publication_year=1949)
>>> print(book)
1984 by George Orwell (1949)


>>> from bookshelf.models import Book
>>> book = Book.objects.get(title ="1984")
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> print(book)
1984 by George Orwell (1949)


 from bookshelf.models import Book     
>>> books = Book.objects.all()       
>>> for book in books:
...     print(book.title, "-", book.author, "-", book.publication_year)


... 