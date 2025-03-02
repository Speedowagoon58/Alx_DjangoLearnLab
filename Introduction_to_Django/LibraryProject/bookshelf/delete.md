from bookshelf.models import Book book = Book.objects.get(title="Nineteen Eighty-Four") book.delete() Book.objects.exists() # Checks if any books exist
