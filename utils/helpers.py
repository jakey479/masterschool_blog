from datetime import datetime


def return_timestamp():
    current_datetime = datetime.now()
    # Format the datetime as a string without seconds
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")
    return formatted_datetime
