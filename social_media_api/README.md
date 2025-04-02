# Social Media API

A Django REST Framework-based social media API with user authentication, posts, and comments functionality.

## Setup Instructions

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install django djangorestframework django-filter Pillow
```

3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
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

- **Response**: Returns user data and authentication token

#### Get user profile

- **URL**: `/api/users/profile/`
- **Method**: `GET`
- **Headers**: `Authorization: Token your_token`
- **Response**: Returns user profile data

#### Update user profile

- **URL**: `/api/users/{id}/`
- **Method**: `PUT` or `PATCH`
- **Headers**: `Authorization: Token your_token`
- **Data**: Any user fields to update
- **Response**: Returns updated user data

### Posts

#### List all posts

- **URL**: `/api/posts/`
- **Method**: `GET`
- **Query Parameters**:
  - `page`: Page number for pagination
  - `search`: Search posts by title or content
  - `ordering`: Order by created_at or updated_at
  - `author`: Filter by author ID

#### Create a new post

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

#### Get a specific post

- **URL**: `/api/posts/{id}/`
- **Method**: `GET`

#### Update a post

- **URL**: `/api/posts/{id}/`
- **Method**: `PUT` or `PATCH`
- **Headers**: `Authorization: Token your_token`
- **Data**: Any post fields to update

#### Delete a post

- **URL**: `/api/posts/{id}/`
- **Method**: `DELETE`
- **Headers**: `Authorization: Token your_token`

### Comments

#### List all comments

- **URL**: `/api/comments/`
- **Method**: `GET`
- **Query Parameters**:
  - `page`: Page number for pagination
  - `post`: Filter by post ID
  - `author`: Filter by author ID
  - `search`: Search in comment content

#### Add a comment to a post

- **URL**: `/api/posts/{post_id}/comment/`
- **Method**: `POST`
- **Headers**: `Authorization: Token your_token`
- **Data**:

```json
{
  "content": "Comment content"
}
```

#### Update a comment

- **URL**: `/api/comments/{id}/`
- **Method**: `PUT` or `PATCH`
- **Headers**: `Authorization: Token your_token`
- **Data**: Any comment fields to update

#### Delete a comment

- **URL**: `/api/comments/{id}/`
- **Method**: `DELETE`
- **Headers**: `Authorization: Token your_token`

## Features

1. User Authentication:

   - Token-based authentication
   - User registration and profile management

2. Posts:

   - Create, read, update, and delete posts
   - Search posts by title or content
   - Filter posts by author
   - Order posts by creation or update time
   - Pagination support

3. Comments:
   - Add comments to posts
   - Update and delete comments
   - Filter comments by post or author
   - Search in comment content
   - Pagination support

## Permissions

- Authentication is required for creating posts and comments
- Users can only edit or delete their own posts and comments
- Anyone can view posts and comments
- Profile updates require authentication

## Error Handling

The API returns appropriate HTTP status codes:

- 200: Successful request
- 201: Resource created
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource not found
- 500: Server error

## User Model

The custom user model includes the following fields:

- username
- email
- bio
- profile_picture
- followers (ManyToMany relationship with other users)
