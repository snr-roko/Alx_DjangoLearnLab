book = Book.objects.get(title = "Nineteen Eighty-Four")
book.delete()

all_books = Book.objects.get(title = "Nineteen Eighty-Four")
print(all_books)

<QuerySet []>