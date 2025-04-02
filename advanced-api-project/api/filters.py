import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    """
    Custom filter for Book model with advanced filtering options.

    This filter provides comprehensive filtering capabilities for the Book model,
    allowing users to filter books by various attributes such as title, author,
    publication year, and more.

    Filtering options:
    - title: Case-insensitive contains search on book title
    - publication_year: Exact match on publication year
    - publication_year_gt: Books published after the specified year
    - publication_year_lt: Books published before the specified year
    - author: Exact match on author ID
    - author_name: Case-insensitive contains search on author name
    - created_after: Books created after the specified date
    - created_before: Books created before the specified date
    """

    title = django_filters.CharFilter(lookup_expr="icontains")
    publication_year_gt = django_filters.NumberFilter(
        field_name="publication_year", lookup_expr="gt"
    )
    publication_year_lt = django_filters.NumberFilter(
        field_name="publication_year", lookup_expr="lt"
    )
    author_name = django_filters.CharFilter(
        field_name="author__name", lookup_expr="icontains"
    )
    created_after = django_filters.DateFilter(
        field_name="created_at", lookup_expr="date__gte"
    )
    created_before = django_filters.DateFilter(
        field_name="created_at", lookup_expr="date__lte"
    )

    class Meta:
        model = Book
        fields = {
            "author": ["exact"],
            "publication_year": ["exact"],
        }
