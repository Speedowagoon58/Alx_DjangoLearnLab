from django.urls import path
from . import views
from . import auth_views

app_name = "relationship_app"

urlpatterns = [
    # Existing URLs
    path("books/", views.book_list, name="book_list"),
    path("books/text/", views.book_list_text, name="book_list_text"),
    path("libraries/", views.LibraryListView.as_view(), name="library_list"),
    path(
        "libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"
    ),
    # Role-based URLs
    path("admin-dashboard/", views.admin_view, name="admin_dashboard"),
    path("librarian-dashboard/", views.librarian_view, name="librarian_dashboard"),
    path("member-dashboard/", views.member_view, name="member_dashboard"),
    # Authentication URLs
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="registration/logged_out.html"),
        name="logout",
    ),
    path("register/", auth_views.register_view, name="register"),
    # Book management URLs
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]

["add_book/", "edit_book/"]
["from .views import list_books"]