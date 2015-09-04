import logging


from rest_framework import generics

from api.serializers import ActorSerializer, MovieSerializer
from movies.models import *

logger = logging.getLogger(__name__)


class ActorListView(generics.ListCreateAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class ActorDetailView(generics.RetrieveAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class MovieListView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class MovieDetailView(generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()