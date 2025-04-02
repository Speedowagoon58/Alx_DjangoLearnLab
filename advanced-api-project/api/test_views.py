from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book
from django.utils import timezone
import json


class BookAPITests(TestCase):
    """
    Test suite for the Book API endpoints.
    Tests CRUD operations, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        """
        Set up test data and client.
        Creates test users, authors, and books.
        """
        # Create test users
        self.admin_user = User.objects.create_user(
            username="admin", password="adminpass", is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username="user", password="userpass"
        )
        self.anonymous_user = None

        # Create test authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create test books
        self.book1 = Book.objects.create(
            title="Book One", publication_year=2020, author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Book Two", publication_year=2021, author=self.author1
        )
        self.book3 = Book.objects.create(
            title="Another Book", publication_year=2019, author=self.author2
        )

        # Set up API client
        self.client = APIClient()

    def test_list_books(self):
        """
        Test retrieving the list of books.
        Should return all books with status 200.
        """
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)

    def test_create_book_authenticated(self):
        """
        Test creating a book with an authenticated user.
        Should create the book and return status 201.
        """
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("book-list")
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author1.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "New Book")

    def test_create_book_unauthenticated(self):
        """
        Test creating a book without authentication.
        Should return status 401.
        """
        url = reverse("book-list")
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author1.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_invalid_year(self):
        """
        Test creating a book with an invalid publication year (future year).
        Should return status 400.
        """
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("book-list")
        future_year = timezone.now().year + 1
        data = {
            "title": "New Book",
            "publication_year": future_year,
            "author": self.author1.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        """
        Test retrieving a specific book.
        Should return the book with status 200.
        """
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_update_book_authenticated(self):
        """
        Test updating a book with an authenticated user.
        Should update the book and return status 200.
        """
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("book-detail", args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 2020,
            "author": self.author1.id,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book1.id).title, "Updated Title")

    def test_update_book_unauthenticated(self):
        """
        Test updating a book without authentication.
        Should return status 401.
        """
        url = reverse("book-detail", args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 2020,
            "author": self.author1.id,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.get(id=self.book1.id).title, self.book1.title)

    def test_delete_book_authenticated(self):
        """
        Test deleting a book with an authenticated user.
        Should delete the book and return status 204.
        """
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_delete_book_unauthenticated(self):
        """
        Test deleting a book without authentication.
        Should return status 401.
        """
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 3)

    def test_filter_books_by_author(self):
        """
        Test filtering books by author.
        Should return only books by the specified author.
        """
        url = reverse("book-list")
        response = self.client.get(f"{url}?author={self.author1.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)
        for book in response.data["results"]:
            self.assertEqual(book["author"], self.author1.id)

    def test_filter_books_by_publication_year(self):
        """
        Test filtering books by publication year.
        Should return only books published in the specified year.
        """
        url = reverse("book-list")
        response = self.client.get(f"{url}?publication_year=2020")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["publication_year"], 2020)

    def test_filter_books_by_title(self):
        """
        Test filtering books by title.
        Should return only books with titles containing the search term.
        """
        url = reverse("book-list")
        response = self.client.get(f"{url}?title=Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)
        for book in response.data["results"]:
            self.assertIn("Book", book["title"])

    def test_search_books(self):
        """
        Test searching books by title or author name.
        Should return books matching the search term.
        """
        url = reverse("book-list")
        response = self.client.get(f"{url}?search=Another")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Another Book")

    def test_order_books_by_title(self):
        """
        Test ordering books by title.
        Should return books in alphabetical order by title.
        """
        url = reverse("book-list")
        response = self.client.get(f"{url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data["results"]]
        self.assertEqual(titles, sorted(titles))

    def test_order_books_by_publication_year_desc(self):
        """
        Test ordering books by publication year in descending order.
        Should return books in descending order by publication year.
        """
        url = reverse("book-list")
        response = self.client.get(f"{url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data["results"]]
        self.assertEqual(years, sorted(years, reverse=True))

    def test_bulk_create_books(self):
        """
        Test bulk creating books.
        Should create multiple books at once and return status 201.
        """
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("book-bulk")
        data = [
            {
                "title": "Bulk Book 1",
                "publication_year": 2022,
                "author": self.author1.id,
            },
            {
                "title": "Bulk Book 2",
                "publication_year": 2022,
                "author": self.author2.id,
            },
        ]
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 5)

    def test_bulk_delete_books(self):
        """
        Test bulk deleting books.
        Should delete multiple books at once and return status 204.
        """
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("book-bulk")
        data = {"ids": [self.book1.id, self.book2.id]}
        response = self.client.delete(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


class AuthorAPITests(TestCase):
    """
    Test suite for the Author API endpoints.
    Tests CRUD operations, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        """
        Set up test data and client.
        Creates test users and authors.
        """
        # Create test users
        self.admin_user = User.objects.create_user(
            username="admin", password="adminpass", is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username="user", password="userpass"
        )
        self.anonymous_user = None

        # Create test authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Set up API client
        self.client = APIClient()

    def test_list_authors(self):
        """
        Test retrieving the list of authors.
        Should return all authors with status 200.
        """
        url = reverse("author-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_create_author_authenticated(self):
        """
        Test creating an author with an authenticated user.
        Should create the author and return status 201.
        """
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("author-list")
        data = {"name": "New Author"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 3)
        self.assertEqual(Author.objects.get(id=response.data["id"]).name, "New Author")

    def test_create_author_unauthenticated(self):
        """
        Test creating an author without authentication.
        Should return status 401.
        """
        url = reverse("author-list")
        data = {"name": "New Author"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Author.objects.count(), 2)

    def test_retrieve_author(self):
        """
        Test retrieving a specific author.
        Should return the author with status 200.
        """
        url = reverse("author-detail", args=[self.author1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.author1.name)

    def test_update_author_authenticated(self):
        """
        Test updating an author with an authenticated user.
        Should update the author and return status 200.
        """
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("author-detail", args=[self.author1.id])
        data = {"name": "Updated Name"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.get(id=self.author1.id).name, "Updated Name")

    def test_update_author_unauthenticated(self):
        """
        Test updating an author without authentication.
        Should return status 401.
        """
        url = reverse("author-detail", args=[self.author1.id])
        data = {"name": "Updated Name"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Author.objects.get(id=self.author1.id).name, self.author1.name)

    def test_delete_author_authenticated(self):
        """
        Test deleting an author with an authenticated user.
        Should delete the author and return status 204.
        """
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("author-detail", args=[self.author1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 1)

    def test_delete_author_unauthenticated(self):
        """
        Test deleting an author without authentication.
        Should return status 401.
        """
        url = reverse("author-detail", args=[self.author1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Author.objects.count(), 2)

    def test_search_authors(self):
        """
        Test searching authors by name.
        Should return authors matching the search term.
        """
        url = reverse("author-list")
        response = self.client.get(f"{url}?search=One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Author One")

    def test_order_authors_by_name(self):
        """
        Test ordering authors by name.
        Should return authors in alphabetical order by name.
        """
        url = reverse("author-list")
        response = self.client.get(f"{url}?ordering=name")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        names = [author["name"] for author in response.data["results"]]
        self.assertEqual(names, sorted(names))

 ["APITestCase"]
["self.client.login"]