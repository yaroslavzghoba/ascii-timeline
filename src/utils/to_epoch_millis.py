from typing import Optional, Dict
from datetime import datetime, timezone, timedelta
from model.timestamp import Timestamp
from utils.constants import Constants


def _is_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def _get_days_in_month(year: int, month: int) -> int:
    """
    Calculates the number of days for a specific month in a specific year.

    Parameters
    ----------
    year: int
        Year to which the month belongs.
    month: int
        The month for which the number of days should be calculated. 
        The value should be in range [1, 12]

    Returns
    -------
    A number of days for a specific month in a specific year.

    Raises
    ------
    ValueError
        If the month value is invalid. 
    """
    if month == 2:
        return 29 if _is_leap(year) else 28
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    raise ValueError(f"Invalid month: {month}")
    

def _get_days_from_civil(year: int, month: int, day: int) -> int:
    """
    Calculates the number of days from 1970-01-01 to a given date.

    The implementation is based on the `days_from_civil` alg. from the standard C++ library <chrono>.
    Reference: https://howardhinnant.github.io/date_algorithms.html#days_from_civil

    
    Parameters
    ----------
    year: int
        Year component of the date for which the number of days from the civil date should be calculated.
    month: int
        Month component of the date for which the number of days from the civil date should be calculated.
        The value should be within the range [1, 12].
    day: int
        Day component of the date for which the number of days from the civil date should be calculated.
        The value should be within the range [1, _days_in_month(year, month)].

    Returns
    -------
    A number of days since 1970-01-01 to a given date.
    """

    # Сonsider March as the first month of the year.
    year -= (1 if month <= 2 else 0)

    # Calculate an era. An era is a complete 400-year cycle.
    if year >= 0:
        era = year // 400
    else:
        era = (year - 399) // 400

    # Year in the current 400-year cycle [0, 399].
    year_of_era = year - era * 400
    # Day in the year [0, 365]. Shift months. 
    if month > 2:
        month_adjust = month - 3
    else:
        month_adjust = month + 9
    day_of_year = (153 * month_adjust + 2) // 5 + day - 1

    # Day in the current 400-year cycle [0, 146096].
    doe = year_of_era * 365 + year_of_era // 4 - year_of_era // 100 + day_of_year

    # Days since 1970-01-01
    return era * 146097 + doe - 719468


def to_epoch_millis(timestamp: Timestamp) -> int:
    """
    Calculates the number of milliseconds from 1970-01-01 00:00:00.000 to the given timestamp.
    If the given timestamp is less than the civil date, the result will be negative.


    Parameters
    ----------
    timestamp: Timestamp
        The point in time to which the number of days from the civil date will be calculated.

    Returns
    -------
    A number of days from 1970-01-01 00:00:00.000 to the given timestamp.

    Raises
    ------
    ValueError
        If one or more components of the given timestamp are invalid.
    """

    # Validate passed values
    if not (1 <= timestamp.month <= 12):
        raise ValueError(f"Invalid month: {timestamp.month}")
    days_in_month = _get_days_in_month(timestamp.year, timestamp.month)
    if not (1 <= timestamp.day <= days_in_month):
        raise ValueError(f"Invalid day {timestamp.day} for {timestamp.year}-{timestamp.month}; The value should be in range [0, {days_in_month}]")
    if not (0 <= timestamp.hour <= 23):
        raise ValueError(f"Invalid hour: {timestamp.hour}; The value should be in range [0, 23]")
    if not (0 <= timestamp.minute <= 59):
        raise ValueError(f"Invalid minute: {timestamp.minute}; The value should be in range [0, 59]")
    if not (0 <= timestamp.second <= 59):
        raise ValueError(f"Invalid second: {timestamp.second}; The value should be in range [0, 59]")
    if not (0 <= timestamp.millisecond <= 999):
        raise ValueError(f"Invalid millisecond: {timestamp.millisecond}; The value should be in range [0, 999]")

    days_from_civil = _get_days_from_civil(timestamp.year, timestamp.month, timestamp.day)
    total_ms = (days_from_civil * Constants.MS_PER_DAY +
                timestamp.hour * Constants.MS_PER_HOUR +
                timestamp.minute * Constants.MS_PER_MINUTE +
                timestamp.second * Constants.MS_PER_SECOND +
                timestamp.millisecond)
    return total_ms

