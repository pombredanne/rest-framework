from django.core.management.base import BaseCommand
import datetime

from movies.models import Actor, Movie


class Command(BaseCommand):

    def handle(self, *args, **options):
        for x in range(1, 8):
            name = 'Actor Number {num}'.format(num=x)
            Actor(name=name, date_of_birth=datetime.datetime.now().date()).save()

        for x in range(1, 6):
            title = 'a random movie about {num}'.format(num=x)
            movie = Movie(title=title, year_released=2012,
            description='a nice new movie from our friends at paramount')
            movie.save()

            for actor in Actor.objects.all().order_by('?')[:2]:
                movie.actors.add(actor)
            movie.save()
