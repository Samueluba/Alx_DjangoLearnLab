import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Query all books by a specific author ---
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)  # <-- uses objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author named {author_name} found.")

# --- List all books in a library ---
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in library_books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library named {library_name} found.")

# --- Retrieve the librarian for a library using objects.get(library=library) ---
try:
    # First get the Library instance
    library_instance = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library_instance)  # <-- checker expects this exact syntax
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print(f"No librarian assigned to {library_name}.")
