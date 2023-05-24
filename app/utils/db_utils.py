from app.models import Movie, Genre, MovieGenre, Actor, MovieActor, Director, MovieDirector
from app import db
from datetime import datetime

def add_movie(wiki_id, movie_label, imdb_id, publication_date):
    new_movie = None
    existing_movie = Movie.query.filter_by(wiki_id=wiki_id).first()
    
    if not existing_movie:
        pub_date_obj = datetime.strptime(publication_date, "%Y-%m-%dT%H:%M:%SZ")
        new_movie = Movie(
            wiki_id=wiki_id,
            imdb_id=imdb_id,
            title=movie_label,
            pubdate=pub_date_obj.date()
        )
        db.session.add(new_movie)

    return [existing_movie or new_movie, new_movie is not None]

def add_genre(wiki_id, genre_label, movie):
    existing_genre = Genre.query.filter_by(wiki_id=wiki_id).first()

    if existing_genre:
        movie_genre = MovieGenre(movie_id=movie.id, genre_id=existing_genre.id)
        db.session.add(movie_genre)
    else:
        new_genre = Genre(name=genre_label, wiki_id=wiki_id)
        db.session.add(new_genre)
        movie_genre = MovieGenre(movie_id=movie.id, genre_id=new_genre.id)
        db.session.add(movie_genre)

def add_actor(wiki_id, actor_label, movie):
    existing_actor = Actor.query.filter_by(wiki_id=wiki_id).first()

    if existing_actor:
        movie_actor = MovieActor(movie_id=movie.id, actor_id=existing_actor.id)
        db.session.add(movie_actor)
    else:
        new_actor = Actor(name=actor_label, wiki_id=wiki_id)
        db.session.add(new_actor)
        movie_actor = MovieActor(movie_id=movie.id, actor_id=new_actor.id)
        db.session.add(movie_actor)

def add_director(wiki_id, director_label, movie):
    existing_director = Director.query.filter_by(wiki_id=wiki_id).first()

    if existing_director:
        movie_director = MovieDirector(movie_id=movie.id, director_id=existing_director.id)
        db.session.add(movie_director)
    else:
        new_director = Director(name=director_label, wiki_id=wiki_id)
        db.session.add(new_director)
        movie_director = MovieDirector(movie_id=movie.id, director_id=new_director.id)
        db.session.add(movie_director)

def commit_changes():
    db.session.commit()
