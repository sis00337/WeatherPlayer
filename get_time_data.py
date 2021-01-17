
import datetime


def get_time():
    """
    Obtain current hour from user's system and display a greeting according to time.

    :return: an appropriate greeting depending on time of day
    """
    user_time = datetime.datetime.now()
    current_hour = user_time.hour

    if current_hour in range(1, 13):
        return "Good morning"
    elif current_hour in range(12, 18):
        return "Good afternoon"
    elif current_hour in range(17, 25):
        return "Good evening"
    else:
        return "Hello"
