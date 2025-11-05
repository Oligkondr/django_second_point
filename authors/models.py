from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
