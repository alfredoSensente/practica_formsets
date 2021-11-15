from django.db import models

# Create your models here.
class Author(models.Model):
    """Model definition for author."""

    name_author = models.CharField(max_length=45)

    class Meta:
        """Meta definition for author."""
        db_table = 'author'
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        """Unicode representation of author."""
        return self.name_author


class Book(models.Model):
    """Model definition for book."""

    book_name = models.CharField(max_length=80)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        db_column='id_author'
    )

    class Meta:
        """Meta definition for book."""
        db_table = 'book'
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        """Unicode representation of book."""
        return self.book_name

