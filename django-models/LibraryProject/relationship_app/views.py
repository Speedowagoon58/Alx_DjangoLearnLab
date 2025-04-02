from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Book, Library
from django.contrib.auth.decorators import user_passes_test, permission_required
from .forms import BookForm


# Function-based view to list all books
def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Alternative function-based view that returns text instead of HTML
def book_list_text(request):
    books = Book.objects.all()
    response = "Books Available:\n\n"
    for book in books:
        response += f"- {book.title} by {book.author.name}\n"
    return HttpResponse(response, content_type="text/plain")


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "ADMIN"


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "LIBRARIAN"


def is_member(user):
    return user.is_authenticated and user.userprofile.role == "MEMBER"


@user_passes_test(is_admin)
def admin_view(request):
    return render(
        request, "relationship_app/admin_view.html", {"title": "Admin Dashboard"}
    )


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(
        request,
        "relationship_app/librarian_view.html",
        {"title": "Librarian Dashboard"},
    )


@user_passes_test(is_member)
def member_view(request):
    return render(
        request, "relationship_app/member_view.html", {"title": "Member Dashboard"}
    )


@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("relationship_app:book_list")
    else:
        form = BookForm()
    return render(request, "relationship_app/book_form.html", {"form": form})


@permission_required("relationship_app.can_edit_book", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("relationship_app:book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/book_form.html", {"form": form})


@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("relationship_app:book_list")
    return render(request, "relationship_app/book_confirm_delete.html", {"book": book})


# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context data here if needed
        return context


# Alternative class-based view using ListView for all libraries
class LibraryListView(ListView):
    model = Library
    template_name = "relationship_app/library_list.html"
    context_object_name = "libraries"

["from django.contrib.auth.decorators import permission_required", "relationship_app.can_change_book"]
["from .models import Library"]
["from django.views.generic.detail import DetailView"]
["from django.contrib.auth import login", "from django.contrib.auth.forms import UserCreationForm"]
["UserCreationForm()", "relationship_app/register.html"]