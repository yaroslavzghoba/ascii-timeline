import typer
from model.event import toEvent
from ascii_timeline import AsciiTimeline

app = typer.Typer()


@app.command()
def generate():
    # TODO: Fetch the actual data from the JSON file.
    events = [
        {
            "event_label": "Construction of the Parthenon in Athens",
            "show_event_label": True,
            "event_timestamp": "-438-09" # Approximately finished in 438 BCE
        },
        {
            "event_label": "Creation of the Code of Justinian",
            "show_event_label": False,
            "event_timestamp": "529"
        },
        {
            "event_label": "Coronation of Charlemagne as Emperor",
            "show_event_label": True,
            "event_timestamp": "800-12-25"
        },
        {
            "event_label": "Invention of the movable type by Johannes Gutenberg",
            "show_event_label": False,
            "event_timestamp": "1440"
        },
        {
            "event_label": "Start of the Reformation (Luther's 95 Theses)",
            "show_event_label": True,
            "event_timestamp": "1517-10-31"
        },
        {
            "event_label": "American Declaration of Independence",
            "show_event_label": False,
            "event_timestamp": "1776-07-04"
        },
        {
            "event_label": "Publication of Darwin's 'On the Origin of Species'",
            "show_event_label": True,
            "event_timestamp": "1859-11-24"
        },
        {
            "event_label": "First flight by the Wright Brothers",
            "show_event_label": False,
            "event_timestamp": "1903-12-17T10:35:00"
        },
        {
            "event_label": "Founding of the United Nations (UN)",
            "show_event_label": True,
            "event_timestamp": "1945-10-24"
        },
        {
            "event_label": "Launch of the World Wide Web to the public",
            "show_event_label": True,
            "event_timestamp": "1991-08-06"
        },
        {
            "event_label": "First successful cloning of a mammal (Dolly the sheep)",
            "show_event_label": False,
            "event_timestamp": "1996-07-05"
        }
    ]

    events = list(map(toEvent, events))
    AsciiTimeline.generate(events=events, length=50)


if __name__ == "__main__":
    app()