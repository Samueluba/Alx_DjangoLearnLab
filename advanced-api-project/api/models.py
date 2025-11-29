from django.db import models

class Author(models.Model):
    """
    The Author model stores the name of the author.
    """
    name = models.CharField(max_length=255)  # Author's full name

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model stores information about a book, including its title,
    publication year, and a reference to the author (foreign key).
    """
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Link to the Author

    def __str__(self):
        return self.title
