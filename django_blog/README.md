# Django Blog Project

A full-featured blog application built with Django, featuring user authentication and CRUD operations for blog posts.

## Features

### User Authentication
- User registration with email verification
- Login and logout functionality
- Profile management
- Secure password handling

### Blog Post Management
- Create, read, update, and delete blog posts
- Rich text content support
- Author attribution
- Creation and update timestamps

### Comments
- Comment on blog posts
- Real-time comment updates
- Author attribution for comments
- Timestamp tracking

### Security Features
- CSRF protection
- Login required for protected actions
- Author-only post editing and deletion
- Secure password hashing

## URL Structure

### Authentication URLs
- `/login/` - User login
- `/logout/` - User logout
- `/register/` - User registration
- `/profile/` - User profile management

### Blog Post URLs
- `/posts/` - List all blog posts
- `/posts/new/` - Create a new post
- `/posts/<int:pk>/` - View post details
- `/posts/<int:pk>/edit/` - Edit a post
- `/posts/<int:pk>/delete/` - Delete a post

## Models

### Post Model
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
```

### Comment Model
```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
```

## Permissions

### Post Permissions
- Create: Authenticated users only
- Read: All users
- Update: Post author only
- Delete: Post author only

### Comment Permissions
- Create: Authenticated users only
- Read: All users
- Update: Not implemented (future feature)
- Delete: Not implemented (future feature)

## Testing

To test the blog post features:

1. Create a new post:
   ```bash
   # Login to your account
   # Click "Create New Post"
   # Fill in the title and content
   # Submit the form
   ```

2. View posts:
   ```bash
   # Visit /posts/ to see all posts
   # Click on a post title to view its details
   ```

3. Edit a post:
   ```bash
   # View your post
   # Click "Edit Post"
   # Make changes and save
   ```

4. Delete a post:
   ```bash
   # View your post
   # Click "Delete Post"
   # Confirm the deletion
   ```

5. Test permissions:
   ```bash
   # Try to edit/delete posts you don't own
   # Verify that only authenticated users can create posts
   # Check that only post authors can edit/delete their posts
   ```

## Development

### Prerequisites
- Python 3.8+
- Django 5.2+
- Django REST Framework 3.16+

### Setup
1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Run migrations
5. Start the development server

### Commands
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 