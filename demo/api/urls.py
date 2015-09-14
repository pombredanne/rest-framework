from django.conf.urls import url


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api import views


@api_view(('GET',))
def api_root(request, format=None):
    """
    Root display view. For help/docs only.
    :param request:
    :param format:
    :return:
    """

    movie_directory = {
        'movies': reverse('api-movies-list', request=request, format=format),
        'movie_by_id': reverse('api-movie-detail', args=['1'], request=request, format=format),
        'actors': reverse('api-actors-list', request=request, format=format),
        'actor_by_id': reverse('api-actor-detail', args=['1'], request=request, format=format)
    }

    api_directory = {'Movie APIs': movie_directory}

    return Response(api_directory)


urlpatterns = [
    url(r'^movies/$', api_root),
    url(r'^movies/actor/(?P<pk>\d+)/$', views.ActorDetailView.as_view(), name='api-actor-detail'),
    url(r'^movies/actor/$', views.ActorListView.as_view(), name='api-actors-list'),

    url(r'^movies/movie/(?P<pk>\d+)/$', views.MovieDetailView.as_view(), name='api-movie-detail'),
    url(r'^movies/movie/$', views.MovieListView.as_view(), name='api-movies-list'),
]
