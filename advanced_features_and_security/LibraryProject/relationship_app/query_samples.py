from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Explicitly using objects.filter()
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No author found with name '{author_name}'"

def list_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"No library found with name '{library_name}'"

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:

        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return library.librarian.name if library.librarian else "No librarian assigned"
    except Library.DoesNotExist:
        return f"No library found with name '{library_name}'"

if __name__ == "__main__":
    # Sample queries
    print("Books by Author 'J.K. Rowling':", query_books_by_author("J.K. Rowling"))
    print("Books in 'Central Library':", list_books_in_library("Central Library"))
    print("Librarian of 'Central Library':", get_librarian_for_library("Central Library"))