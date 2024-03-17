from django.db import models

# Create your models here.

class Rating(models.Model):
    numReviews=models.IntegerField()
    avgRating=models.FloatField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length = 255)
    description= models.CharField(max_length=255)
    rating=models.ForeignKey( Rating ,on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    publicationDate = models.DateField(verbose_name='Publication date', auto_now_add=True)
    tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
 

 