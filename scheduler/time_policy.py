from datetime import datetime

START_HOUR = 0
END_HOUR = 24

def is_within_allowed_time():
    hour = datetime.now().hour
    return START_HOUR <= hour < END_HOUR
