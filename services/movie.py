from typing import List

from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
):
    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        )

    if genres_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        )

    if actors_ids:
        queryset = queryset.filter(
            actors__id__in=actors_ids
        )

    return queryset


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
):
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,

    )
    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
    return new_movie
