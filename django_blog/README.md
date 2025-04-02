# Django Blog Project

A comprehensive blog application built with Django, featuring user authentication, blog post management, comments, and advanced features like tagging and search.

## Features

- User Authentication

  - Registration
  - Login/Logout
  - Profile Management

- Blog Post Management

  - Create, Read, Update, Delete (CRUD) operations
  - Rich Text Editor
  - Post Categories and Tags

- Comments System

  - Add comments to posts
  - Edit/Delete comments
  - Comment moderation

- Advanced Features
  - Search functionality
  - Tag-based filtering
  - User notifications

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd django_blog
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

## Project Structure

```
django_blog/
├── blog/                   # Main application directory
│   ├── migrations/        # Database migrations
│   ├── static/           # Static files (CSS, JS, Images)
│   ├── templates/        # HTML templates
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── urls.py          # URL configurations
│   └── forms.py         # Form classes
├── django_blog/          # Project configuration
│   ├── settings.py      # Project settings
│   ├── urls.py         # Main URL configuration
│   └── wsgi.py         # WSGI configuration
├── templates/            # Global templates
├── static/              # Global static files
├── media/               # User-uploaded files
├── requirements.txt     # Project dependencies
└── manage.py           # Django management script
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
