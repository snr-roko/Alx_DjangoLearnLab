# views.py

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View to list all books in the database.

    Methods:
        GET: Returns a list of all books.

    Permissions:
        Allows read-only access to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required for read-only access.


class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by its ID.

    Methods:
        GET: Returns details of a single book.

    Permissions:
        Allows read-only access to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required for read-only access.


class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book in the database.

    Methods:
        POST: Creates a new book with the provided data.

    Permissions:
        Requires authentication. Only authenticated users can create new books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create.


class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.

    Methods:
        PUT: Updates the entire book.
        PATCH: Partially updates the book.

    Permissions:
        Requires authentication. Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update.


class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book from the database.

    Methods:
        DELETE: Removes the specified book.

    Permissions:
        Requires authentication. Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete.
