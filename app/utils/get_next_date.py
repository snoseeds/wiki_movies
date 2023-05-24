from datetime import timedelta

def get_next_date(date_obj):
    # Calculate the next date by adding one day
    return date_obj + timedelta(days=1)
    
