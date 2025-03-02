# Import Django setup to run standalone scripts
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

# Import models
from relationship_app.models import Author, Book, Library, Librarian


def create_sample_data():
    """Create sample data to demonstrate relationships"""
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")

    # Create books
    book1 = Book.objects.create(title="Harry Potter", author=author1)
    book2 = Book.objects.create(title="Fantastic Beasts", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)

    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")

    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2, book3)
    library2.books.add(book2, book4)

    # Create librarians (OneToOne relationship)
    librarian1 = Librarian.objects.create(name="John Smith", library=library1)
    librarian2 = Librarian.objects.create(name="Sarah Johnson", library=library2)

    print("Sample data created successfully!")


def query_books_by_author(author_name):
    """Query all books by a specific author (ForeignKey relationship)"""
    try:
        author = Author.objects.get(name=author_name)

        # Required string: objects.filter(author=author)
        books = Book.objects.filter(author=author)

        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"- {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def list_books_in_library(library_name):
    """List all books in a library (ManyToMany relationship)"""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()

        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library (OneToOne relationship)"""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using the related_name from OneToOneField

        print(f"\nLibrarian for {library_name}:")
        print(f"- {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")
        return None


if __name__ == "__main__":
    # First create sample data
    create_sample_data()

    # Execute sample queries
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    get_librarian_for_library("Community Library")

    # Documentation for Django ORM queries
    print("\nDjango ORM Query Examples:")
    print("1. ForeignKey: Book.objects.filter(author=author)")
    print("2. ManyToMany: library.books.all()")
    print("3. OneToOne: library.librarian")

    objects.filter(author=author)
