from app.services.movie_service import MovieService
from flask import request
from app.dtos.sync_movies_input import SyncMoviesInput
from app import app

# Movie controller
class MovieController:
    @app.route("/")
    def index():
        return "Hello World, welcome to the Wiki Movies Endpoints!"

    @app.route("/sync_movies", methods=["POST"])
    def sync_movies():
        try:
            data = request.get_json()
            start_date = data.get("startDate")
            end_date = data.get("endDate")
            input_data = SyncMoviesInput(start_date, end_date)
            try:
                input_data.validate()

                # Perform synchronization with the provided start_date and end_date
                result = MovieService.sync_movies(start_date, end_date)
                if result is True:
                    return "Movies synchronized successfully!"
                else:
                    return "There's error syncing the movies", 500
            except ValueError as e:
                return str(e), 400
        except Exception as e:
            return f"Something went wrong {str(e)}", 500

movie_controller = MovieController()
