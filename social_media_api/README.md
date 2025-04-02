# Social Media API

A Django REST Framework-based social media API with user authentication and profile management.

## Setup Instructions

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install django djangorestframework
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

## Authentication

The API uses token-based authentication. Include the token in the request header:

```
Authorization: Token your_token
```

## User Model

The custom user model includes the following fields:

- username
- email
- bio
- profile_picture
- followers (ManyToMany relationship with other users)
