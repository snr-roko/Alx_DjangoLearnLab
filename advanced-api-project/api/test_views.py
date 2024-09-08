# test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):
    """
    Test suite for CRUD operations and query functionalities of the Book API.
    """

    def setUp(self):
        """
        Set up the test environment. This includes creating users, authors, and book instances.
        """
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create an author
        self.author = Author.objects.create(name='Author One')

        # Create some books
        self.book1 = Book.objects.create(title='Book One', publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title='Book Two', publication_year=2021, author=self.author)

    def test_list_books(self):
        """
        Test the retrieval of all books.
        """
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_retrieve_book(self):
        """
        Test the retrieval of a single book by its ID.
        """
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book(self):
        """
        Test creating a new book.
        """
        data = {'title': 'New Book', 'publication_year': 2023, 'author': self.author.pk}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')

    def test_update_book(self):
        """
        Test updating an existing book.
        """
        data = {'title': 'Updated Book', 'publication_year': 2022, 'author': self.author.pk}
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """
        Test filtering books by title.
        """
        response = self.client.get(reverse('book-list') + '?title=Book One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books(self):
        """
        Test searching books by title and author name.
        """
        response = self.client.get(reverse('book-list') + '?search=Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get(reverse('book-list') + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')
        self.assertEqual(response.data[1]['title'], 'Book Two')

    def test_permission_denied_for_unauthenticated_user(self):
        """
        Test that unauthenticated users cannot create, update, or delete books.
        """
        self.client.logout()
        create_response = self.client.post(reverse('book-create'), {'title': 'Unauthorized Book', 'publication_year': 2023, 'author': self.author.pk})
        self.assertEqual(create_response.status_code, status.HTTP_401_UNAUTHORIZED)

        update_response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.pk}), {'title': 'Unauthorized Update', 'publication_year': 2022, 'author': self.author.pk})
        self.assertEqual(update_response.status_code, status.HTTP_401_UNAUTHORIZED)

        delete_response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book1.pk}))
        self.assertEqual(delete_response.status_code, status.HTTP_401_UNAUTHORIZED)
