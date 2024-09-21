# Authentication Documentation

## Introduction
The authentication system in this Django application is designed to manage user accounts securely, allowing users to register, log in, log out, and manage their profiles. This documentation provides an overview of each component and how users interact with them.

## Authentication Components

### User Model
- **Custom User Model**: The application uses a custom user model, `CustomUser`, which extends Django's built-in `AbstractUser`. This model allows for additional fields such as profile pictures and bios, ensuring flexibility in user data management.

### Registration Process
- Users can register by filling out a registration form that extends Django’s `UserCreationForm`. 
- **Validation Checks**: The form ensures that the username and email are unique, and it provides feedback on validation errors.
- **View**: The registration view processes the form and creates a new user upon successful validation and redirects to login for the user to login with the new credentials.

### Login Process
- Users log in using the `LoginView`, which handles authentication through username and password.
- **CSRF Protection**: A CSRF token is included in the login form to prevent cross-site request forgery.
- **Session Management**: Upon successful login, the user is redirected to the homepage or a specified page.

### Logout Process
- Users can log out using the `LogoutView`, which terminates their session.
- **Redirection**: After logging out, users are redirected to the login page or another specified page.

### Profile Management
- Authenticated users can view and edit their profile details through a dedicated profile view.
- **Profile Form**: A custom form is used to update user information, allowing changes to fields like email, profile picture, and bio.
- **View Logic**: The profile view handles GET requests to display current user data and POST requests to update it.

### Permissions and Access Control
- The `@login_required` decorator is used to restrict access to certain views (e.g., profile and posts) to authenticated users only.
- Unauthorized access attempts redirect users to the login page.

## User Interaction Flow

1. **Registration**: 
   - Users navigate to the `/register/` URL and fill out the registration form.
   - Upon successful registration, they receive a confirmation message and can log in.
  
2. **Login**:
   - Users go to the `/login/` URL and enter their credentials.
   - Successful login redirects them to the homepage; failed attempts show error messages.
  
3. **Profile Update**:
   - After logging in, users can access their profile at the `/profile/` URL.
   - They can update their details and submit the form, with feedback on success or errors.
  
4. **Logout**:
   - Users log out via the `/logout/` URL, which ends their session and redirects them to the login page.

## Conclusion
This authentication system ensures secure user management and interaction within the application. For any issues or feedback, users are encouraged to reach out for support.
