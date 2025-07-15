from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.URLField()
    imdb_rating = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    runtime = models.CharField(max_length=20)
    likes = models.ManyToManyField(User, related_name='liked_movies', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Cast(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField()
    bio = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='casts')

    def __str__(self):
        return self.name

