import requests
from django.conf import settings

def get_access_token():
    data = {
        'grant_type': 'client_credentials',
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
    }
    response = requests.post(settings.PROLOGS_TOKEN_URL, data=data)
    response_data = response.json()
    return response_data.get('access_token')

from datetime import datetime, timedelta

def plan_optimal_schedule(pickup_time, dropoff_time, last_rest_time):
    # Assuming pickup_time, dropoff_time, and last_rest_time are datetime objects
    driving_time = (dropoff_time - pickup_time).total_seconds() / 3600
    duty_period = (dropoff_time - last_rest_time).total_seconds() / 3600  # This should really be from the start of the day

    if driving_time > 11:
        return False, "Exceeds 11-hour driving limit."

    # Correctly check if the end of the duty period is within the 14-hour window from the start of duty
    if (pickup_time - last_rest_time).total_seconds() / 3600 > 14:
        return False, "Exceeds 14-hour window."

    if driving_time > 8:
        needed_rest = 2  # Assuming an 8/2 split for simplicity
        return False, f"Needs at least {needed_rest} hours of rest due to driving over 8 hours."

    return True, "Schedule within HOS regulations."



def detect_hos_violations(driving_time, hours_since_last_rest):
    messages = []
    valid = True

    if driving_time > 11:
        valid = False
        messages.append("Driving time exceeds 11 hours.")
    
    if hours_since_last_rest + driving_time > 14:
        valid = False
        messages.append("Total duty period exceeds 14 hours.")

    if not valid:
        # Example adjustment suggestion
        messages.append("Consider reducing driving hours or adding rest periods.")
    
    return valid, messages

def validate_datetime(date_text):
    try:
        return datetime.strptime(date_text, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return None
