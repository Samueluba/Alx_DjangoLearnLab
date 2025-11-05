from django.db import models


class Author(models.Model):
    """Represents an author who can write many books."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """A book written by one author (ForeignKey)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author.name}"


class Library(models.Model):
    """A library that contains many books (ManyToMany)."""
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name


class Librarian(models.Model):
    """Each library has exactly one librarian (OneToOne)."""
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"{self.name} - Librarian of {self.library.name}"

