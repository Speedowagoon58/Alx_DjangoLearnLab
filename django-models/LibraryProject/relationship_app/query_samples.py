# Import Django setup to run standalone scripts
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
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
        
        # Using objects.filter(author=author) as required
        books = Book.objects.filter(author=author)
        
        print(f"\nBooks by {author_name} (using objects.filter):")
        for book in books:
            print(f"- {book.title}")
            
        # Alternative approach using the related_name
        related_books = author.books.all()
        print(f"\nBooks by {author_name} (using related_name):")
        for book in related_books:
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

def additional_filter_examples():
    """Additional examples of using filter()"""
    print("\nAdditional filter examples:")
    
    # Filter books with titles containing "Harry"
    harry_books = Book.objects.filter(title__contains="Harry")
    print("Books with 'Harry' in the title:")
    for book in harry_books:
        print(f"- {book.title}")
    
    # Filter libraries with more than 2 books
    libraries_with_many_books = Library.objects.filter(books__gt=2).distinct()
    print("\nLibraries with more than 2 books:")
    for library in libraries_with_many_books:
        print(f"- {library.name} ({library.books.count()} books)")
    
    # Get all authors who have books in Central Library
    central_library = Library.objects.get(name="Central Library")
    authors_in_central = Author.objects.filter(books__libraries=central_library).distinct()
    print("\nAuthors with books in Central Library:")
    for author in authors_in_central:
        print(f"- {author.name}")

if __name__ == "__main__":
    # First create sample data
    create_sample_data()
    
    # Execute sample queries
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    get_librarian_for_library("Community Library")
    
    # Additional examples showing reverse relationships
    print("\nLibraries containing 'Fantastic Beasts':")
    book = Book.objects.get(title="Fantastic Beasts")
    for library in book.libraries.all():
        print(f"- {library.name}")
    
    print("\nLibrary managed by 'John Smith':")
    librarian = Librarian.objects.get(name="John Smith")
    print(f"- {librarian.library.name}")
    
    # Run additional filter examples
    additional_filter_examples()

    ["Librarian.objects.get(library="]
    "Librarian.objects.get(library="
     Librarian.objects.get(library=