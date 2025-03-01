from django.contrib import admin
from .models import Author, Book, Library, Librarian

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

# Example usage in shell
from relationship_app.models import Author, Book, Library, Librarian

# Create an author
author = Author.objects.create(name="J.K. Rowling")

# Create a book
book = Book.objects.create(title="Harry Potter", author=author)

# Create a library
library = Library.objects.create(name="City Library")
library.books.add(book)

# Create a librarian
librarian = Librarian.objects.create(name="John Doe", library=library)
