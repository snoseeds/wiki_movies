# wiki_movies
This is a guide on how to install and use the **wiki_movies** application.

## Installation

# Clone the repository
- git clone wiki_movies
- cd wiki_movies

# Activate the virtual environment
- python3 -m venv venv 

# Install dependencies into the virtual env
- pip install -r requirements.txt

# Start a Docker-powered PostgreSQL container and database:
- docker run --name movies_db -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres-
- docker exec -it movies_db createdb -U postgres wiki_movies

# Apply migrations in the application:
- python manage.py db upgrade

## Usage
- To run the app, use the following command:
- flask run
Visit http://127.0.0.1:5000 to see the app.

## Postman Detailed Documentation with Examples
For detailed documentation and examples, please refer to the [Postman Documentation](https://documenter.getpostman.com/view/6777319/2s93m4ZPXY).

## Contact
For any inquiries or feedback, feel free to reach out to:
Nurudeen Soremekun (nurudeen.soremekun@gmail.com)



