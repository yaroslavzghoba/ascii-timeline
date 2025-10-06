from typing import Optional


class Timestamp:
    """Contains date and time components that can be used to refer to a specific point in time."""

    def __init__(self, year: int, month: int = 1, day: int = 1, hour: int = 0, 
                 minute: int = 0, second: int = 0, millisecond: int = 0):
        self.year = year
        self.month = month
        self.day = day
        self.minute = minute
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond


    def __repr__(self):
        date = f"{self.year:04}-{self.month:02}-{self.day:02}"
        time = f"{self.hour:02}:{self.minute:02}:{self.second:02}.{self.millisecond:03}"
        return f"{date} {time}"
