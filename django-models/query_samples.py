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
