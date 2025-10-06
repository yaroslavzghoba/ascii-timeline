from typing import Dict
from model.timestamp import Timestamp
from utils.constants import Constants
from utils.timestamp_parser import TimestampParser


class Event:
    """An event in time that can be placed on a timeline."""

    def __init__(self, label: str, show_label: bool, timestamp: Timestamp):
        self.label = label
        self.show_label = show_label
        self.timestamp = timestamp


def toEvent(event: Dict[str, str]) -> Event:
    label = event[Constants.EVENT_LABEL_KEY]
    show_label = event[Constants.SHOW_EVENT_LABEL_KEY]
    timestamp = TimestampParser.parse(event[Constants.EVENT_TIMESTAMP_KEY])
    return Event(label=label, show_label=show_label, timestamp=timestamp)