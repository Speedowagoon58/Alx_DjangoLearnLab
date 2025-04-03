# Social Media API

A Django REST Framework-based social media API with user authentication, posts, comments, likes, and notifications functionality.

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

### Likes

#### Like a post

- **URL**: `/api/posts/{post_id}/like/`
- **Method**: `POST`
- **Headers**: `Authorization: Token your_token`
- **Response**: Returns like object with user and post information

#### Unlike a post

- **URL**: `/api/posts/{post_id}/unlike/`
- **Method**: `POST`
- **Headers**: `Authorization: Token your_token`
- **Response**: Empty response with 204 status code

### Notifications

#### List all notifications

- **URL**: `/api/notifications/`
- **Method**: `GET`
- **Headers**: `Authorization: Token your_token`
- **Query Parameters**:
  - `page`: Page number for pagination

#### Get unread notifications count

- **URL**: `/api/notifications/unread_count/`
- **Method**: `GET`
- **Headers**: `Authorization: Token your_token`
- **Response**:

```json
{
  "count": 5
}
```

#### Mark notification as read

- **URL**: `/api/notifications/{notification_id}/mark_read/`
- **Method**: `POST`
- **Headers**: `Authorization: Token your_token`

#### Mark all notifications as read

- **URL**: `/api/notifications/mark_all_read/`
- **Method**: `POST`
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

4. Likes:

   - Like and unlike posts
   - Track likes count per post
   - Check if current user has liked a post

5. Notifications:
   - Receive notifications for:
     - New likes on posts
     - New comments on posts
     - New followers
   - Mark notifications as read
   - Get unread notifications count
   - Pagination support

## Permissions

- Authentication is required for creating posts, comments, and likes
- Users can only edit or delete their own posts and comments
- Users can only like a post once
- Users can only access their own notifications
- Anyone can view posts and comments
- Profile updates require authentication

## Error Handling

The API returns appropriate HTTP status codes:

- 200: Successful request
- 201: Resource created
- 204: No content (successful deletion)
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

## Models

1. User Model:

   - Custom user model with bio and profile picture
   - Followers relationship

2. Post Model:

   - Title and content
   - Author relationship
   - Created and updated timestamps
   - Likes relationship

3. Comment Model:

   - Content
   - Post and author relationships
   - Created and updated timestamps

4. Like Model:

   - User and post relationships
   - Created timestamp
   - Unique constraint on user-post combination

5. Notification Model:
   - Recipient and actor relationships
   - Notification type (like, comment, follow)
   - Target object (generic relationship)
   - Read status
   - Created timestamp
