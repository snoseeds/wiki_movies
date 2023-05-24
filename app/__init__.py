from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config.from_pyfile("../config.py")

db = SQLAlchemy(app)

from app.models import Movie, Genre, MovieGenre, Actor, MovieActor, Director, MovieDirector
from app.controllers import movie_controller

