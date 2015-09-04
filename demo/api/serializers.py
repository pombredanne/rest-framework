import logging

from rest_framework import serializers
from movies.models import Movie, Actor

logger = logging.getLogger(__name__)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'date_of_birth')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie