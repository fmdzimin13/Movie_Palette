from django.db import models
from django.conf import settings

# Create your models here.
# class Genre(models.Model):
#     name = models.CharField(max_length=50)


# class Movie(models.Model):

#   title = models.CharField(max_length=100)
#   link =models.CharField(max_length=200)
#   image = models.CharField(max_length=200)
#   pub_date = models.DateTimeField()
#   user_rating = models.IntegerField()
#   overview = models.TextField(default='', blank=True)


class Movie(models.Model):
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, related_name='like_movies')
    adult = models.BooleanField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    vote_average = models.IntegerField()
    # poster_path = 'https://image.tmdb.org/t/p/w500' + str(models.CharField(max_length=200))
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200, null=True)
    custom_genre = models.IntegerField()
    wordcloud = models.ImageField(blank=True)




