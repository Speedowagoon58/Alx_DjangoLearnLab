from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes custom validation for the publication_year field.
    """

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "publication_year",
            "author",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate_publication_year(self, value):
        """
        Check that the publication year is not in the future
        """
        if value > timezone.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future"
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested representation of all books by this author.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def to_representation(self, instance):
        """
        Customize the output representation to include the number of books
        """
        representation = super().to_representation(instance)
        representation["books_count"] = instance.books.count()
        return representation
