import re
from datetime import datetime
from app import app

class SyncMoviesInput:
    DATE_FORMAT = r"^\d{4}-\d{2}-\d{2}$"

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    @classmethod
    def validate_start_date(cls, start_date):
        earliest_sync_date = app.config["EARLIEST_DATE_TO_SYNC"]

        min_date_obj = datetime.strptime(earliest_sync_date, "%Y-%m-%d").date()
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        if start_date_obj < min_date_obj:
            raise ValueError(f"Start date cannot be earlier than {earliest_sync_date}")

    def validate_date_format(self, date):
        if not re.match(self.DATE_FORMAT, date):
            raise ValueError("Invalid date format. Date must be in 'yyyy-mm-dd' format.")

    def validate(self):
        self.validate_date_format(self.start_date)
        self.validate_date_format(self.end_date)
        self.validate_start_date(self.start_date)
        if self.start_date > self.end_date:
            raise ValueError("Start date must be less than or equal to end date")