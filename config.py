import os

# Database configuration
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysecretpassword@localhost:5432/wiki_movies'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuration settings
IMDB_BASE_URL = "https://www.imdb.com/title/"
WIKIDATA_ENDPOINT = "https://query.wikidata.org/sparql"
WIKIDATA_BASE_URL = "http://www.wikidata.org/entity/"
EARLIEST_DATE_TO_SYNC = "2014-01-01"
SECRET_KEY = 'your_secret_key'

# Ensure the required directories exist
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

os.environ['FLASK_ENV'] = 'development'

