# Social Media API

A Django REST Framework-based social media API with user authentication, posts, comments, likes, and notifications functionality.

## Local Development Setup

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a .env file:

```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

## Production Deployment

### Prerequisites

- A Heroku account
- Heroku CLI installed
- Git installed
- PostgreSQL database (can be provisioned through Heroku)

### Deployment Steps

1. Login to Heroku:

```bash
heroku login
```

2. Create a new Heroku app:

```bash
heroku create your-app-name
```

3. Add PostgreSQL addon:

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. Configure environment variables:

```bash
heroku config:set DJANGO_SECRET_KEY=your-secret-key
heroku config:set DJANGO_DEBUG=False
heroku config:set DJANGO_ALLOWED_HOSTS=.herokuapp.com
heroku config:set DJANGO_SECURE_SSL_REDIRECT=True
heroku config:set DJANGO_SESSION_COOKIE_SECURE=True
heroku config:set DJANGO_CSRF_COOKIE_SECURE=True
heroku config:set DJANGO_SECURE_HSTS_SECONDS=31536000
heroku config:set DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=True
heroku config:set DJANGO_SECURE_HSTS_PRELOAD=True
heroku config:set DJANGO_CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

5. Deploy to Heroku:

```bash
git add .
git commit -m "Prepare for deployment"
git push heroku main
```

6. Run migrations on Heroku:

```bash
heroku run python manage.py migrate
```

7. Create a superuser on Heroku (optional):

```bash
heroku run python manage.py createsuperuser
```

### Maintenance

1. Monitor application logs:

```bash
heroku logs --tail
```

2. Scale dynos if needed:

```bash
heroku ps:scale web=1
```

3. Regular updates:

```bash
# Update dependencies locally
pip install -r requirements.txt --upgrade
# Update requirements.txt
pip freeze > requirements.txt
# Commit and deploy
git add requirements.txt
git commit -m "Update dependencies"
git push heroku main
```

## API Endpoints

### User Authentication

#### Register a new user

- **URL**: `/api/users/`
- **Method**: `POST`
- **Data**:

```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password",
  "password2": "your_password",
  "bio": "Your bio"
}
```

#### Get user profile

- **URL**: `/api/users/profile/`
- **Method**: `GET`
- **Headers**: `Authorization: Token your_token`

### Posts

#### List all posts

- **URL**: `/api/posts/`
- **Method**: `GET`
- **Query Parameters**:
  - `page`: Page number
  - `search`: Search posts
  - `ordering`: Order by created_at or updated_at
  - `author`: Filter by author ID

#### Create a post

- **URL**: `/api/posts/`
- **Method**: `POST`
- **Headers**: `Authorization: Token your_token`
- **Data**:

```json
{
  "title": "Post Title",
  "content": "Post content"
}
```

### Likes

#### Like a post

- **URL**: `/api/posts/{post_id}/like/`
- **Method**: `POST`
- **Headers**: `Authorization: Token your_token`

#### Unlike a post

- **URL**: `/api/posts/{post_id}/unlike/`
- **Method**: `POST`
- **Headers**: `Authorization: Token your_token`

### Notifications

#### List notifications

- **URL**: `/api/notifications/`
- **Method**: `GET`
- **Headers**: `Authorization: Token your_token`

#### Mark notification as read

- **URL**: `/api/notifications/{notification_id}/mark_read/`
- **Method**: `POST`
- **Headers**: `Authorization: Token your_token`

## Security Features

- Token-based authentication
- HTTPS enforcement
- XSS protection
- CSRF protection
- Content-Type sniffing prevention
- HSTS (HTTP Strict Transport Security)
- Secure cookie settings
- CORS configuration

## Monitoring and Logging

The application uses Django's built-in logging configuration and can be monitored through:

1. Heroku's built-in logging:

```bash
heroku logs --tail
```

2. Django's logging system (configured in settings.py)

3. Heroku's metrics dashboard

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
