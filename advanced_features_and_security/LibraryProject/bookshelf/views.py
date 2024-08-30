from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from .forms import ExampleForm

# Example view enforcing permissions
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return HttpResponse(f"Book Title: {book.title}")

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Book Created")
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# View to list all books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse(f"Book with ID {book_id} Edited")
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return HttpResponse(f"Book with ID {book_id} Deleted")
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})
