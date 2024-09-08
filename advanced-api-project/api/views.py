# views.py

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    View to list all books in the database with advanced query capabilities.

    Methods:
        GET: Returns a list of all books.

    Permissions:
        Allows read-only access to both authenticated and unauthenticated users.

    Features:
        - Filtering: Users can filter books by title, author, and publication_year.
        - Searching: Users can search books by title and author's name.
        - Ordering: Users can order books by title and publication_year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only access for unauthenticated users.
    
    # Enabling filtering, searching, and ordering capabilities
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Fields available for filtering
    search_fields = ['title', 'author__name']  # Fields available for search
    ordering_fields = ['title', 'publication_year']  # Fields available for ordering
    ordering = ['title']  # Default ordering by title


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
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only access for unauthenticated users.


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
    permission_classes = [IsAuthenticated]  # Only authenticated users can create.


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
    permission_classes = [IsAuthenticated]  # Only authenticated users can update.


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
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete.
