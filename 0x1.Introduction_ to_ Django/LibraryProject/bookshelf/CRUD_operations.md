new_book = Book.objects.create(title= "1984", author = "George Orwell", publication_year = 1949)
new_book.save()

no output



all_books = Book.objects.all()
print(all_books)

<QuerySet [<Book: Book object (1)>]>



book = Book.objects.get(title = "1984")
book.title = "Nineteen Eighty-Four"
book.save()

No Output



book = Book.objects.get(title = "Nineteen Eighty-Four")
book.delete()

book = Book.objects.get(title= "Nineteen Eighty-Four")
print(book)

<QuerySet []>

