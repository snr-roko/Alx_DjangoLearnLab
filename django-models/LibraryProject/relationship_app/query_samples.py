from . import models

# Querying all books by a specific Author

author = models.Author.objects.get(name = '')
books_by_author = author.books.all()

for book in books_by_author:
  print(book.name)


# Listing all books in a Library
library = models.Library.objects.get(name = '')
books_in_a_library = library.books.all()

for book in books_in_a_library:
  print(book.name)

# Retrieving the Librarian for a library
library = models.Library.objects.get(name = '')
librarian_for_the_library = library.librarian
print(librarian_for_the_library.name)