from relationship_app.models import Author, Book, Library, Librarian


# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Reverse lookup using related_name
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
        return books
    except Author.DoesNotExist:
        print("Author not found.")
        return []


# 2️⃣ List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name}:")
        for book in books:
            print(f"- {book.title}")
        return books
    except Library.DoesNotExist:
        print("Library not found.")
        return []


# 3️⃣ Retrieve the librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # OneToOne reverse relation
        print(f"Librarian of {library.name}: {librarian.name}")
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or Librarian not found.")
        return None

