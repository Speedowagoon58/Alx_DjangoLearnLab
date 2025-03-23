from django.db import models
from api.models import Book


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


INSTALLED_APPS = [
    # ...existing apps...
    "api",
]

# Run the following commands to apply migrations
# python manage.py makemigrations
# python manage.py migrate

book = Book.objects.create(title="Sample Book", author="Author Name")
print(book)
