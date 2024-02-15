import time

def get_time() -> str:
    """
    Gets the current time and returns it as a str

    Example: '01:05:03 (10/02/24)'
    """

    return time.strftime('%X (%d/%m/%y)')