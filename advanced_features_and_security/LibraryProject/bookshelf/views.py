from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from .forms import BookForm, ExampleForm

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
<<<<<<< Tabnine <<<<<<<
@permission_required('bookshelf.can_view', raise_exception=True)#+
def view_book(request, book_id):#+
    """#+
    This function retrieves a book from the database based on the provided book_id and displays its title.#+
#+
    Parameters:#+
    request (HttpRequest): The incoming request object.#+
    book_id (int): The unique identifier of the book to retrieve.#+
#+
    Returns:#+
    HttpResponse: An HTTP response containing the title of the book if found, or a 404 error if the book is not found.#+
    """#+
    book = get_object_or_404(Book, id=book_id)#+
    return HttpResponse(f"Book Title: {book.title}")#+
>>>>>>> Tabnine >>>>>>>