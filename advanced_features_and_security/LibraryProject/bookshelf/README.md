# LibraryProject - Bookshelf App

## Overview
This project involves managing a library system with custom user models, permissions, and groups.

## Custom User Model
The `CustomUser` model extends Django's `AbstractUser` model with additional fields:
- `date_of_birth`: A date field to store the user's birth date.
- `profile_photo`: An image field to store the user's profile photo.

### Custom User Manager
- `create_user`: Manages the creation of regular users with the additional fields.
- `create_superuser`: Manages the creation of superusers and ensures required fields are set.

## Permissions and Groups

### Custom Permissions
The `Book` model includes custom permissions:
- `can_view`: Allows viewing of book details.
- `can_create`: Allows creation of new book entries.
- `can_edit`: Allows editing of existing book entries.
- `can_delete`: Allows deletion of book entries.

### Groups
- **Editors**: Assigned `can_create` and `can_edit` permissions.
- **Viewers**: Assigned `can_view` permission.
- **Admins**: Assigned all permissions including `can_delete`.

## Views with Permission Checks
The `book_list` view in `views.py` checks for the `can_view` permission before listing books.

```python
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# LibraryProject - Bookshelf App

## Security Best Practices

### 1. Settings Configuration
The following security settings have been applied in `settings.py`:

- **DEBUG**: Set to `False` in production to prevent sensitive information from being displayed in error pages.
- **SECURE_BROWSER_XSS_FILTER**: Enabled to prevent cross-site scripting attacks by the browser.
- **X_FRAME_OPTIONS**: Set to `DENY` to prevent clickjacking by disallowing the site to be loaded in an iframe.
- **SECURE_CONTENT_TYPE_NOSNIFF**: Enabled to prevent MIME type sniffing.
- **CSRF_COOKIE_SECURE**: Ensures that CSRF cookies are only sent over HTTPS.
- **SESSION_COOKIE_SECURE**: Ensures that session cookies are only sent over HTTPS.
- **Content Security Policy (CSP)**: Configured using Django's CSP middleware to limit the domains from which content can be loaded.

### 2. Views and Forms Security
- **CSRF Protection**: All forms include the `{% csrf_token %}` tag to protect against CSRF attacks.
- **Safe Data Handling**: Views use Django's ORM with `get_object_or_404` and forms to validate and sanitize user inputs, protecting against SQL injection and other data-related vulnerabilities.

### 3. Content Security Policy (CSP)
The Content Security Policy (CSP) is configured to only allow content from the application’s domain and trusted sources. This mitigates the risk of XSS attacks by restricting where scripts and other resources can be loaded from.

### 4. Testing and Validation
To ensure these security measures are effective, the following steps were taken:

- **CSRF Testing**: Forms were tested for proper token inclusion, and submissions were checked to verify protection against CSRF attacks.
- **XSS Testing**: Inputs were tested to confirm that CSP and other browser protections block malicious scripts.
- **SQL Injection Testing**: Queries were tested to ensure that they are properly parameterized and protected against SQL injection attempts.
