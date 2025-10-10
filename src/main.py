import os
import json
import typer
from typing_extensions import Annotated
from typing import Optional, List, Dict, Any
from model.event import toEvent
from utils.constants import Constants
from ascii_timeline import AsciiTimeline


app = typer.Typer()


@app.command()
def generate(
    events_file_path: str,
    length: Annotated[Optional[int], typer.Option()] = Constants.TIMELINE_LENGTH_DEFAULT,
):
    # TODO: Fetch the actual data from the JSON file.
    events: List[Dict[str, Any]] = []
    if os.path.isfile(events_file_path):
        with open(events_file_path) as file:
            events = json.loads(file.read())
    else:
        return

    events = list(map(toEvent, events))
    AsciiTimeline.generate(events, length)


if __name__ == "__main__":
    app()