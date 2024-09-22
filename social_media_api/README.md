# Django User API

This Django REST API project provides endpoints for user registration, authentication, and profile management.

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### User Registration

- **URL:** `/api/accounts/register/`
- **Method:** POST
- **Data Params:** 
  ```json
  {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "username": "johndoe",
    "profile_picture": "<file>",
    "bio": "A short bio",
    "password1": "securepassword",
    "password2": "securepassword"
  }
  ```
- **Success Response:** HTTP 201 Created

### User Login

- **URL:** `/api/accounts/login/`
- **Method:** POST
- **Data Params:** 
  ```json
  {
    "email": "john@example.com",
    "password": "securepassword"
  }
  ```
- **Success Response:** HTTP 200 OK
  ```json
  {
    "token": "<auth_token>"
  }
  ```

### User Profile

- **URL:** `/api/accounts/profile/<user_id>`
- **Method:** GET
- **Headers:** Authorization: Token <auth_token>
- **Success Response:** HTTP 200 OK
  ```json
  {
    "profile_picture": "<url>",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe"
  }
  ```

## User Model

The custom user model (`CustomUser`) extends Django's `AbstractUser` and includes the following additional fields:

- `bio`: TextField for user's biography
- `profile_picture`: ImageField for user's profile picture
- `followers`: ManyToManyField for managing user followers

## Authentication

This API uses Token Authentication. Include the token in the Authorization header for authenticated requests:

```
Authorization: Token <your_token_here>
```

## Testing

You can test the API endpoints using tools like Postman or curl. Make sure to include the necessary headers and data as specified in the API documentation.
In Postman, make sure to set Authorization to Token <your token> as a header instead of using Authorization tab.