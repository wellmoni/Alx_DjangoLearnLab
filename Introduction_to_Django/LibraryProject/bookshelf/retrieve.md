# Retrieve Book Entry

```python
books = Book.objects.all()
for book in books:
    print(book.title, "-", book.author, "-", book.publication_year)
