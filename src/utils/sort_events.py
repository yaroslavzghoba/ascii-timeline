from typing import List, Tuple
from model.event import Event


def sort_events(events: List[Event]) -> List[Event]:
    """
    Sorts a list of events by the timestamp column in ascending chronological order.

    
    Parameters
    ----------
    events : List[Event])
        A list of events to be sorted.

    Returns
    -------
    A sorted list of events by the timestamp column.
    """

    def timestamp_key(event: Event) -> Tuple[int, int, int, int, int, int, int]:
        return (
            event.timestamp.year,
            event.timestamp.month,
            event.timestamp.day,
            event.timestamp.hour,
            event.timestamp.minute,
            event.timestamp.second,
            event.timestamp.millisecond,
        )


    return sorted(events, key=timestamp_key)