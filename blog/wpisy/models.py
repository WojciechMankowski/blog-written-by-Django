from django.db import models
from django.utils import timezone


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Autor = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    Zajawka = models.CharField(max_length=200)
    Body_postu = models.TextField()
    IMG = models.TextField()

    def __str__(self):
        return self.Title

    def was_published_recently(self):
        pass


class kontakt(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Title = models.CharField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.Title
