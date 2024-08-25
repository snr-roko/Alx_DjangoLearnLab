from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book

# Example view enforcing permissions
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return HttpResponse(f"Book Title: {book.title}")

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic to create a book
    return HttpResponse("Book Created")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    return HttpResponse(f"Book with ID {book_id} Edited")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Logic to delete a book
    return HttpResponse(f"Book with ID {book_id} Deleted")
