from django.db import models
from authors.models import Author


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books_author')
    isbn = models.CharField(max_length=100, unique=True)
    publication_year = models.IntegerField()
    genres = models.ManyToManyField('Genre', blank=True)
    co_authors = models.ManyToManyField(
        Author,
        blank=True,
        related_name='books_co_author')
    summary = models.TextField(blank=True)


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
