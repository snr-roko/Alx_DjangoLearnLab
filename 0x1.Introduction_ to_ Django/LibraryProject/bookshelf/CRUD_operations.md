new_book = Book("1984", "George Orwell", 1949)
new_book.save()

no output



all_books = Book.objects.all()
print(all_books)

<QuerySet [<Book: Book object (1)>]>



book_to_update = Book.objects.get(title = "1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

No Output



book_to_delete = Book.objects.get(title = "Nineteen Eighty-Four")
book_to_delete.delete()

all_books = Book.objects.all()
print(all_books)

<QuerySet []>

