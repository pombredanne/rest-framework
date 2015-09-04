from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=120)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=120)
    year_released = models.IntegerField()
    description = models.TextField()
    actors = models.ManyToManyField(Actor, blank=True)

    def __str__(self):
        return self.title
