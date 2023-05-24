from app import db

# Define the Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    pubdate = db.Column(db.Date)
    wiki_id = db.Column(db.String(20), unique=True)
    imdb_id = db.Column(db.String(20))

# Define the Genre model
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    imdb_id = db.Column(db.String(20))
    wiki_id = db.Column(db.String(20), unique=True)


# Define the MovieGenre model (many-to-many relationship between Movie and Genre)
class MovieGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id", ondelete='CASCADE'))
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete='CASCADE'))

# Define the Actor model
class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    imdb_id = db.Column(db.String(20))
    wiki_id = db.Column(db.String(20), unique=True)

# Define the MovieActor model (many-to-many relationship between Movie and Actor)
class MovieActor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id", ondelete='CASCADE'))
    actor_id = db.Column(db.Integer, db.ForeignKey("actor.id", ondelete='CASCADE'))

# Define the Director model
class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    imdb_id = db.Column(db.String(20))
    wiki_id = db.Column(db.String(20), unique=True)

# Define the MovieDirector model (many-to-many relationship between Movie and Director)
class MovieDirector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id", ondelete='CASCADE'))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id", ondelete='CASCADE'))

# # Define the User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))
#     roles = db.relationship("Role", secondary="user_role", backref="users")

# # Define the Role model
# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))

# # Define the UserRole model (association table between User and Role)
# user_role = db.Table(
#     "user_role",
#     db.Column("user_id", db.Integer, db.ForeignKey("user.id", ondelete='CASCADE'), primary_key=True),
#     db.Column("role_id", db.Integer, db.ForeignKey("role.id", ondelete='CASCADE'), primary_key=True)
# )
