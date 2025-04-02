from django.shortcuts import render
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .filters import BookFilter


# Custom pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


# Custom permission class for book operations
class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a book to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to authenticated users
        return request.user and request.user.is_authenticated


# Custom mixin for logging and tracking operations
class OperationLoggingMixin:
    """
    Mixin to log operations performed on models.
    """

    def perform_create(self, serializer):
        """
        Log the creation of a new object
        """
        instance = serializer.save()
        print(f"Created {instance.__class__.__name__}: {instance}")
        return instance

    def perform_update(self, serializer):
        """
        Log the update of an existing object
        """
        instance = serializer.save()
        print(f"Updated {instance.__class__.__name__}: {instance}")
        return instance

    def perform_destroy(self, instance):
        """
        Log the deletion of an object
        """
        print(f"Deleted {instance.__class__.__name__}: {instance}")
        instance.delete()


# Create your views here.


class AuthorListCreateView(OperationLoggingMixin, generics.ListCreateAPIView):
    """
    API endpoint for listing all authors and creating new authors.
    GET: List all authors
    POST: Create a new author
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name", "created_at"]


class AuthorDetailView(OperationLoggingMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific author.
    GET: Retrieve a specific author
    PUT/PATCH: Update a specific author
    DELETE: Delete a specific author
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookListCreateView(OperationLoggingMixin, generics.ListCreateAPIView):
    """
    API endpoint for listing all books and creating new books.

    GET: List all books with advanced filtering, searching, and ordering capabilities

    Filtering options:
    - author: Filter by author ID (exact match)
    - publication_year: Filter by publication year (exact match)
    - title: Filter by title (case-insensitive contains)
    - publication_year_gt: Books published after the specified year
    - publication_year_lt: Books published before the specified year
    - author_name: Filter by author name (case-insensitive contains)
    - created_after: Books created after the specified date
    - created_before: Books created before the specified date

    Search options:
    - search: Search in title and author name fields

    Ordering options:
    - ordering: Order by title, publication_year, or created_at
    - Use '-' prefix for descending order (e.g., -publication_year)

    Pagination:
    - page: Page number
    - page_size: Number of items per page (max 100)

    POST: Create a new book (authenticated users only)
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = BookFilter
    search_fields = ["title", "author__name"]
    ordering_fields = ["title", "publication_year", "created_at"]

    def get_queryset(self):
        """
        Optionally filter books by author

        This method provides backward compatibility with the old filtering approach
        while also supporting the new DjangoFilterBackend.
        """
        queryset = Book.objects.all()
        author_id = self.request.query_params.get("author", None)
        if author_id is not None:
            queryset = queryset.filter(author_id=author_id)
        return queryset


class BookDetailView(OperationLoggingMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific book.
    GET: Retrieve a specific book
    PUT/PATCH: Update a specific book
    DELETE: Delete a specific book
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        """
        Customize the deletion process
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookBulkOperationsView(APIView):
    """
    Custom view for bulk operations on books.
    POST: Create multiple books at once
    DELETE: Delete multiple books at once
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        Create multiple books at once
        """
        serializer = BookSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Delete multiple books at once
        """
        book_ids = request.data.get("ids", [])
        if not book_ids:
            return Response(
                {"error": "No book IDs provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        books = Book.objects.filter(id__in=book_ids)
        count = books.count()
        books.delete()

        return Response(
            {"message": f"Successfully deleted {count} books"},
            status=status.HTTP_204_NO_CONTENT,
        )


["ListView", "UpdateView", "DeleteView"]
["from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"]
["from django_filters import rest_framework"]