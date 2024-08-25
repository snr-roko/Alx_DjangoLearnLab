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
