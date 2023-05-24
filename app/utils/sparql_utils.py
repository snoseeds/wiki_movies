import asyncio
from SPARQLWrapper import SPARQLWrapper, JSON
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app.utils.db_utils import add_movie, add_genre, add_actor, add_director, commit_changes
from app.utils.file_utils import read_txt_file, overwrite_txt_file
from app import app
from app.utils.get_next_date import get_next_date

async def get_movie_data(start_date, end_date):
    try:
        sparql = SPARQLWrapper(app.config["WIKIDATA_ENDPOINT"])
        
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        while start_date_obj <= end_date_obj:
            # Make the query
            query = f"""
            SELECT ?movie ?movieLabel ?imdbId ?genre ?genreLabel ?actor ?actorLabel ?director ?directorLabel ?publicationDate
            WHERE {{
              ?movie wdt:P577 ?publicationDate ;
                     wdt:P345 ?imdbId .
              FILTER (?publicationDate = "{start_date_obj.strftime("%Y-%m-%d")}"^^xsd:dateTime) .
              OPTIONAL {{ ?movie wdt:P136 ?genre . }}
              OPTIONAL {{ ?movie wdt:P161 ?actor . }}
              OPTIONAL {{ ?movie wdt:P57 ?director . }}
              SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,en" . }}
            }}
            """
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)

            # Fetch the data
            results = sparql.query().convert()

            print(f"this date: {start_date_obj.strftime('%Y-%m-%d')} has {len(results['results']['bindings'])} movie records, not sure of how many uniques yet")

            # Process the chunk of data
            chunk_result, new_movie_insertions_count = process_chunk(results)
            print(f"this date: {start_date_obj.strftime('%Y-%m-%d')} has {new_movie_insertions_count} unique movie records")
            
            if not chunk_result:
                print(f"error processing movies on this date {start_date}")
                return None


            # Delay the next iteration (if needed) to control the rate of fetching data
            # https://api.wikimedia.org/wiki/Documentation/Getting_started/Rate_limits
            # 500 requests = 3600seconds
            # 1 request = 3600 / 500 seconds = 7.2 round to 10seconds
            await asyncio.sleep(10)
            start_date_obj = get_next_date(start_date_obj)
        print("Data fetching completed.")
        return True
    except Exception as e:
        print(f"An error occurred 1: {str(e)}")
        return None

def process_chunk(chunk):
    new_movie_insertions_count = 0
    try:
        for result in chunk['results']['bindings']:
            wiki_id = result["movie"]["value"].split(app.config["WIKIDATA_BASE_URL"])[1]
            movie_label = result["movieLabel"]["value"]
            imdb_id = result["imdbId"]["value"]
            publication_date = result["publicationDate"]["value"]
            
            movie, is_new_movie = add_movie(wiki_id, movie_label, imdb_id, publication_date)
            if is_new_movie:
                new_movie_insertions_count += 1
            
            process_genres(result, movie)
            process_actors(result, movie)
            process_directors(result, movie)

        commit_changes()
        return [True, new_movie_insertions_count]

    except Exception as e:
        print(f"An error occurred 2: {str(e)}")
        return None

def process_genres(result, movie):
    wiki_id = None
    genre_label = None
    try:
        wiki_id = result.get("genre", {}).get("value").split(app.config["WIKIDATA_BASE_URL"])[1]
        genre_label = result.get("genreLabel", {}).get("value")
    except Exception as e:
        print(f"Error occurred retrieving wiki_id and genre_label: {str(e)}")
    
    if wiki_id and genre_label:
        add_genre(wiki_id, genre_label, movie)

def process_actors(result, movie):
    wiki_id = None
    actor_label = None
    try:
        wiki_id = result.get("actor", {}).get("value").split(app.config["WIKIDATA_BASE_URL"])[1]
        actor_label = result.get("actorLabel", {}).get("value")
    except Exception as e:
        print(f"Error occurred retrieving wiki_id and actor_label: {str(e)}")
    
    if wiki_id and actor_label:
        add_actor(wiki_id, actor_label, movie)

def process_directors(result, movie):
    wiki_id = None
    director_label = None
    try:
        wiki_id = result.get("director", {}).get("value").split(app.config["WIKIDATA_BASE_URL"])[1]
        director_label = result.get("directorLabel", {}).get("value")
    except Exception as e:
        print(f"Error occurred retrieving wiki_id and director_label: {str(e)}")
    
    if wiki_id and director_label:
        add_director(wiki_id, director_label, movie)

