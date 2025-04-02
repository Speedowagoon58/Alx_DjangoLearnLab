from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Author(models.Model):
    """
    Author model representing a book author.
    This model stores basic information about authors and maintains
    a one-to-many relationship with books.
    """

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model representing a book in the system.
    This model stores book information and maintains a many-to-one
    relationship with authors. Each book must have an author.
    """

    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """
        Custom validation to ensure publication_year is not in the future
        """
        if self.publication_year > timezone.now().year:
            raise ValidationError(
                {"publication_year": "Publication year cannot be in the future"}
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.publication_year}) by {self.author.name}"
