from django.urls import path
from . import views

urlpatterns = [
    # Author endpoints
    path("authors/", views.AuthorListCreateView.as_view(), name="author-list-create"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    # Book endpoints
    path("books/", views.BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path(
        "books/bulk/",
        views.BookBulkOperationsView.as_view(),
        name="book-bulk-operations",
    ),
]

["books/create", "books/update", "books/delete"]