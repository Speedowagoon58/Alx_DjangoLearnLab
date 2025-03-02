# bookshelf/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ExampleForm  # Ensure ExampleForm is imported
from .models import Book

def submit_book(request):
    """
    View to handle the form submission for adding a new book to the library.
    This view ensures that user inputs are validated and secure.
    """

    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the cleaned data from the form
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            cover = form.cleaned_data['cover']

            # Optionally, you could save this data to the database (for example, to create a new Book object)
            # You can add logic for saving a Book object here
            Book.objects.create(title=title, author=author, cover=cover)

            # Redirect to the book list page after successfully saving the book
            return redirect('book_list')  # Make sure 'book_list' URL name is defined in urls.py
        else:
            # If the form is invalid, render it again with errors
            return render(request, 'bookshelf/form_example.html', {'form': form})
    else:
        # If the method is GET, initialize an empty form
        form = ExampleForm()

    # Render the form for the user to fill out
    return render(request, 'bookshelf/form_example.html', {'form': form})

def book_list(request):
    """
    View to display the list of books in the library.
    Fetches all books from the database and passes them to the template.
    """

    books = Book.objects.all()  # Get all books in the library
    return render(request, 'bookshelf/book_list.html', {'books': books})

def edit_book(request, book_id):
    """
    View to handle the editing of an existing book.
    """
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)

    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()  # Save the updated book object
            return redirect('book_list')
        else:
            return render(request, 'bookshelf/form_example.html', {'form': form})
    else:
        form = ExampleForm(instance=book)

    return render(request, 'bookshelf/form_example.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    """
    View to handle the deletion of a book.
    """
    try:
        book = Book.objects.get(id=book_id)
        book.delete()  # Delete the book from the database
        return redirect('book_list')
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)
