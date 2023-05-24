import asyncio
from app.utils.sparql_utils import get_movie_data
from app.models import Movie


# Movie service
class MovieService:
    def sync_movies(start_date, end_date):
        return asyncio.run(get_movie_data(start_date, end_date))

    def get_movie(movie_id):
        movie = Movie.query.get(movie_id)
        return movie
