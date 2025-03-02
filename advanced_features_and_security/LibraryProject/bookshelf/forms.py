# bookshelf/forms.py

from django import forms
from .models import Book
from django.core.exceptions import ValidationError
import re

class ExampleForm(forms.Form):
    """A generic form for handling user input."""

    title = forms.CharField(max_length=200, required=True, label="Book Title")
    author = forms.CharField(max_length=100, required=True, label="Author Name")
    cover = forms.ImageField(required=False, label="Book Cover")

    def clean_title(self):
        """Validate the title to avoid XSS or other dangerous characters."""
        title = self.cleaned_data.get('title')
        if re.search(r'[<>\"\'%&]', title):
            raise ValidationError('Title contains invalid characters.')
        return title

    def clean_author(self):
        """Validate the author's name to avoid XSS or other dangerous characters."""
        author = self.cleaned_data.get('author')
        if re.search(r'[<>\"\'%&]', author):
            raise ValidationError('Author contains invalid characters.')
        return author

    def clean_cover(self):
        """Ensure that only valid image files are uploaded for the cover."""
        cover = self.cleaned_data.get('cover')
        if cover:
            if not cover.name.endswith(('jpg', 'jpeg', 'png', 'gif')):
                raise ValidationError('Invalid file type for cover. Only image files are allowed.')
        return cover
