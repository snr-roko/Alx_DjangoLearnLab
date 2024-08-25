from .models import Author, Book, Library, Librarian

# Querying all books by a specific Author
def books_by_author(author_name):
  author = Author.objects.get(name=author_name)
  books = Book.objects.filter(author=author)

  for book in books:
    print(book.name)


# Listing all books in a Library
def books_in_a_library(library_name):
  library = Library.objects.get(name=library_name)
  books_in_a_library = library.books.all()

  for book in books_in_a_library:
    print(book.name)

# Retrieving the Librarian for a library
def librarian_for_a_library(library_name):
  librarian = Librarian.objects.get(library=library_name)
  print(librarian.name)