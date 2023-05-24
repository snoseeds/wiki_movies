import logging
from app import app


# Log a message
def log_message(message):
    log_file = app.config["LOG_FILE"]
    logging.basicConfig(filename=log_file, level=logging.INFO)
    logging.info(message)
