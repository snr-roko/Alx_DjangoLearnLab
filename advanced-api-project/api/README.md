# Advanced API Project - View Configuration

## Overview

This project implements a set of Django REST Framework views for the `Book` model, handling CRUD operations efficiently.

### Views

1. **BookListView**:
   - **Purpose**: Lists all books in the database.
   - **Method**: GET
   - **Permissions**: Allows read-only access to everyone.

2. **BookDetailView**:
   - **Purpose**: Retrieves a single book by its ID.
   - **Method**: GET
   - **Permissions**: Allows read-only access to everyone.

3. **BookCreateView**:
   - **Purpose**: Creates a new book.
   - **Method**: POST
   - **Permissions**: Only authenticated users can create new books.

4. **BookUpdateView**:
   - **Purpose**: Updates an existing book.
   - **Methods**: PUT, PATCH
   - **Permissions**: Only authenticated users can update books.

5. **BookDeleteView**:
   - **Purpose**: Deletes a book from the database.
   - **Method**: DELETE
   - **Permissions**: Only authenticated users can delete books.

## Customization and Permissions

- **Permissions**: Create, Update, and Delete views are restricted to authenticated users. Read-only views are open to all.
- **Validation**: Additional validation is implemented in the serializers to ensure correct data handling.
- **Testing**: Tested using Postman to validate CRUD operations and permission enforcement.
