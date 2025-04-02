# Advanced API Project

A Django REST Framework project demonstrating advanced API development with custom serializers and nested relationships.

## Features

- Custom serializers with nested relationships
- Data validation
- Generic views for CRUD operations
- Permission-based access control
- Advanced filtering and search capabilities
- Pagination support
- Custom permission classes
- Ordering and sorting
- Bulk operations
- Operation logging
- Custom view mixins

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

```bash
# Windows
.\venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
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

## API Endpoints

### Authors

- `GET /api/authors/` - List all authors
  - Supports pagination
  - Search by name using `?search=<query>`
  - Order by name or created_at using `?ordering=name` or `?ordering=-created_at`
- `POST /api/authors/` - Create a new author (authenticated users only)
- `GET /api/authors/<id>/` - Retrieve a specific author
- `PUT /api/authors/<id>/` - Update a specific author (authenticated users only)
- `DELETE /api/authors/<id>/` - Delete a specific author (authenticated users only)

### Books

- `GET /api/books/` - List all books
  - Supports pagination
  - Filter by author using `?author=<author_id>`
  - Filter by publication year using `?publication_year=<year>`
  - Filter by title using `?title=<query>`
  - Filter by publication year range using `?publication_year_gt=<year>` and `?publication_year_lt=<year>`
  - Filter by author name using `?author_name=<query>`
  - Filter by creation date using `?created_after=<date>` and `?created_before=<date>`
  - Search by title or author name using `?search=<query>`
  - Order by title, publication_year, or created_at using `?ordering=title` or `?ordering=-publication_year`
- `POST /api/books/` - Create a new book (authenticated users only)
- `GET /api/books/<id>/` - Retrieve a specific book
- `PUT /api/books/<id>/` - Update a specific book (authenticated users only)
- `DELETE /api/books/<id>/` - Delete a specific book (authenticated users only)

### Bulk Operations

- `POST /api/books/bulk/` - Create multiple books at once (authenticated users only)
  - Request body: Array of book objects
- `DELETE /api/books/bulk/` - Delete multiple books at once (authenticated users only)
  - Request body: `{"ids": [1, 2, 3]}`

## Authentication

The API uses Django REST Framework's authentication system:

- Session Authentication
- Basic Authentication

For write operations (POST, PUT, DELETE), authentication is required. Read operations (GET) are available to all users.

## Permissions

- `IsAuthenticatedOrReadOnly`: Allows read access to any user, but write access only to authenticated users
- `IsAuthorOrReadOnly`: Custom permission that only allows authors to modify their own books

## Models

### Author

- name (CharField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

### Book

- title (CharField)
- publication_year (IntegerField)
- author (ForeignKey to Author)
- created_at (DateTimeField)
- updated_at (DateTimeField)

## Serializers

### AuthorSerializer

- Includes nested BookSerializer for related books
- Adds books_count to the representation

### BookSerializer

- Includes custom validation for publication_year
- Prevents future publication years

## Advanced Features

### Pagination

- Default page size: 10 items
- Customizable page size using `?page_size=<size>` (max 100)
- Navigate pages using `?page=<number>`

### Filtering

The API provides comprehensive filtering capabilities for books:

#### Basic Filtering

- Filter books by author ID: `?author=1`
- Filter books by publication year: `?publication_year=2020`

#### Advanced Filtering

- Filter books by title: `?title=django`
- Filter books by publication year range: `?publication_year_gt=2010&publication_year_lt=2020`
- Filter books by author name: `?author_name=smith`
- Filter books by creation date: `?created_after=2023-01-01&created_before=2023-12-31`

#### Implementation Details

Filtering is implemented using Django REST Framework's `DjangoFilterBackend` and a custom `BookFilter` class. The filter class defines various filter fields with specific lookup expressions to provide flexible filtering options.

### Searching

The API provides search functionality for books:

- Search books by title or author name: `?search=django`
- Search authors by name: `?search=smith`

Search is implemented using Django REST Framework's `SearchFilter` and is case-insensitive by default.

### Ordering

The API provides ordering capabilities for books and authors:

- Order books by title: `?ordering=title`
- Order books by publication year (descending): `?ordering=-publication_year`
- Order books by creation date: `?ordering=created_at`
- Order authors by name: `?ordering=name`

Ordering is implemented using Django REST Framework's `OrderingFilter` and supports both ascending and descending order (using the `-` prefix).

### Custom Views and Mixins

- `OperationLoggingMixin`: Logs all create, update, and delete operations
- `BookBulkOperationsView`: Handles bulk creation and deletion of books
- Custom filter classes for advanced filtering

## Testing the API

You can test the API using tools like Postman, curl, or the Django REST Framework browsable API.

### Example curl commands:

1. List all books:

```bash
curl http://localhost:8000/api/books/
```

2. Filter books by publication year:

```bash
curl http://localhost:8000/api/books/?publication_year=2020
```

3. Filter books by title:

```bash
curl http://localhost:8000/api/books/?title=django
```

4. Filter books by publication year range:

```bash
curl http://localhost:8000/api/books/?publication_year_gt=2010&publication_year_lt=2020
```

5. Search books by title or author name:

```bash
curl http://localhost:8000/api/books/?search=django
```

6. Order books by publication year (descending):

```bash
curl http://localhost:8000/api/books/?ordering=-publication_year
```

7. Combine filtering, searching, and ordering:

```bash
curl http://localhost:8000/api/books/?publication_year_gt=2010&search=django&ordering=-publication_year
```

8. Create a new book:

```bash
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"New Book","publication_year":2023,"author":1}'
```

9. Update a book:

```bash
curl -X PUT http://localhost:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Book","publication_year":2023,"author":1}'
```

10. Delete a book:

```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

11. Bulk create books:

```bash
curl -X POST http://localhost:8000/api/books/bulk/ \
  -H "Content-Type: application/json" \
  -d '[{"title":"Book 1","publication_year":2020,"author":1},{"title":"Book 2","publication_year":2021,"author":1}]'
```

12. Bulk delete books:

```bash
curl -X DELETE http://localhost:8000/api/books/bulk/ \
  -H "Content-Type: application/json" \
  -d '{"ids":[1,2,3]}'
```
