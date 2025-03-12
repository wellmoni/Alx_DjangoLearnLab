from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create a book
        self.book = Book.objects.create(title="Sample Book", publication_year=2020, author=self.author)

        # API Endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

    def test_list_books(self):
        """Test retrieving list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_create_book_authenticated(self):
        """Test creating a book when authenticated"""
        self.client.force_authenticate(user=self.user)
        data = {"title": "New Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication"""
        data = {"title": "Unauthorized Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating a book"""
        self.client.force_authenticate(user=self.user)
        data = {"title": "Updated Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books(self):
        """Test filtering books by author name"""
        response = self.client.get(f"{self.list_url}?author__name=John Doe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching for books by title"""
        response = self.client.get(f"{self.list_url}?search=Sample")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by title"""
        response = self.client.get(f"{self.list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
