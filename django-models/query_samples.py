from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()  # Uses related_name='books'
    except Author.DoesNotExist:
        return []


# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()  # ManyToManyField access
    except Library.DoesNotExist:
        return []


# Retrieve the librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # Reverse OneToOneField access
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
import os
import django

# Setup Django environment for standalone script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Queries ---

# 1. Query all books by a specific author
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author named {author_name} found.")

# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in library_books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library named {library_name} found.")

# 3. Retrieve the librarian for a library
try:
    librarian = library.librarian
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}.")
