from . import models

# Querying all books by a specific Author
def books_by_author(author_name):
  author = models.Author.objects.get(name=author_name)
  books_by_author = author.books.all()

  for book in books_by_author:
    print(book.name)


# Listing all books in a Library
def books_in_a_library(library_name):
  library = models.Library.objects.get(name=library_name)
  books_in_a_library = library.books.all()

  for book in books_in_a_library:
    print(book.name)

# Retrieving the Librarian for a library
def librarian_for_a_library(library_name):
  library = models.Library.objects.get(name=library_name)
  librarian_for_the_library = library.librarian
  print(librarian_for_the_library.name)