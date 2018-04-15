from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    continent = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def post_count(self):
        return Post.objects.filter(visiting_places__country1=self).count()

    def last_updated(self):
        return Post.objects.filter(visiting_places__country1=self).order_by('-created_at').first()

class State(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='states',  on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class VisitingPlaces(models.Model):
    place_name = models.CharField(max_length= 50)
    location = models.CharField(max_length = 500)
    starter = models.CharField(max_length = 30)
    last_updated = models.DateTimeField(auto_now_add=True)
    country1 = models.ForeignKey(Country, related_name='vplaces',  on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.place_name

class Post(models.Model):
    message = models.TextField(max_length=4000)
    visiting_places = models.ForeignKey(VisitingPlaces, related_name='posts',  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',  on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
