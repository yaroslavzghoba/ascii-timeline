import re
from typing import Optional, Dict
from model.timestamp import Timestamp


class TimestampParser:
    # TODO: Write a description for the class.

    def parse(timestamp_str: str) -> Dict[str, Optional[int]]:
        # TODO: Write a description for the class.

        # Parse the string if it contains only year.
        match = re.fullmatch(r"([+-]?\d+)", timestamp_str)
        if match:
            return Timestamp(year=int(match.group(1)), month=1, day=1, hour=0, minute=0, 
                             second=0, millisecond=0)

        # Parse the string if it contains only year and month.
        match = re.fullmatch(r"([+-]?\d+)-(\d{2})", timestamp_str)
        if match:
            return Timestamp(year=int(match.group(1)), month=int(match.group(2)), day=1, hour=0, 
                             minute=0, second=0, millisecond=0)

        # Parse the string if it contains the full date, but no time.
        match = re.fullmatch(r"([+-]?\d+)-(\d{2})-(\d{2})", timestamp_str)
        if match:
            return Timestamp(year=int(match.group(1)), month=int(match.group(2)), day=int(match.group(3)), 
                             hour=0, minute=0, second=0, millisecond=0)

        # Parse the string if it contains the full date and time (excluding milliseconds).
        match = re.fullmatch(r"([+-]?\d+)-(\d{2})-(\d{2})[T ](\d{2}):(\d{2}):(\d{2})", timestamp_str)
        if match:
            return Timestamp(year=int(match.group(1)), month=int(match.group(2)), day=int(match.group(3)), 
                             hour=int(match.group(4)), minute=int(match.group(5)), second=int(match.group(6)), 
                             millisecond=0)

        # Parse the string if it contains the full date and time (including milliseconds).
        match = re.fullmatch(r"([+-]?\d+)-(\d{2})-(\d{2})[T ](\d{2}):(\d{2}):(\d{2})\.(\d{1,3})", timestamp_str)
        if match:
            return Timestamp(year=int(match.group(1)), month=int(match.group(2)), day=int(match.group(3)), 
                             hour=int(match.group(4)), minute=int(match.group(5)), second=int(match.group(6)), 
                             millisecond=int(match.group(7)))

        raise ValueError(f"The timestamp cannot be parsed: {timestamp_str}")
