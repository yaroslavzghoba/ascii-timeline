```
   ___   _________________  _______           ___         
  / _ | / __/ ___/  _/  _/ /_  __(_)_ _  ___ / (_)__  ___ 
 / __ |_\ \/ /___/ /_/ /    / / / /  ' \/ -_) / / _ \/ -_)
/_/ |_/___/\___/___/___/   /_/ /_/_/_/_/\__/_/_/_//_/\__/
```

**ASCII Timeline** is a command-line utility for visualizing events on a timeline, even when only the year is known.

### Output example:

```
[1843, the first algorithm by Ada Lovelace]
                                 [1946, the first computer ENIAC]
                                     [1957, the Fortran programming language]
                                          [1972, the C programming language]
                                                [1991, the Python programming language]
                                                       [2011, the Kotlin programming language]
+-----------------------------+--++--++---+---+-++-----+---+
                                                           [2025, today]
                                                 [1995, the Java programming language]
                                              [1985, the C++ programming language]
                                      [1960, the COBOL programming language]
                                  [1947, the Assembler programming language]
                              [1936, the universal machine by Alan Turing]
```

## Usage

1. Install the necessary dependencies using `pip`:

```shell
pip install -r requirements.txt
```

> [!TIP] Python Virtual Environment
> It's good practice to create a separate virtual environment for a project to isolate its dependencies. Read [how to create a new virtual environment](https://docs.python.org/3/library/venv.html) for more details.

2. Create a new JSON file (e.g., `events.json`) and define your events. Each timeline must contain at least two events. The event with the earliest date determines the beginning of the timeline, and the event with the latest date determines its end.

```json
[
    {
        "event_label": "1843, the first algorithm by Ada Lovelace",
        "show_event_label": true,
        "event_timestamp": "1843"
    },
    {
        "event_label": "1936, the universal machine by Alan Turing",
        "show_event_label": true,
        "event_timestamp": "1936"
    }
]
```

As shown above, you only need to specify the year, but more precise formats are supported. See the [supported time formats](README.md#supported-time-formats) for more details.

3. Generate the timeline. Run the main script, passing the desired timeline length and the path to your JSON configuration file:

```shell
python3 ./src/main.py --length 60 ./events.json
```

## Supported Time Formats

**ASCII Timeline** uses an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)-like format, allowing you to specify only the known parts of a date. The program supports the following formats for the `event_timestamp` field:

| Format | Example | Description |
| --- | --- | --- |
| `YYYY` | `2372` | Year only |
| `YYYY-MM` | `2372-12` | Year and month |
| `YYYY-MM-DD` | `2372-12-08` | Year, month, and day |
| `YYYY-MM-DD hh:mm:ss`, `YYYY-MM-DDThh:mm:ss` | `2372-12-08 10:30:56`, `2372-12-08T10:30:56` | Full date and time (excluding milliseconds) |
| `YYYY-MM-DD hh:mm:ss.sss`, `YYYY-MM-DDThh:mm:ss.sss` | `2372-12-08 10:30:56.376`, `2372-12-08T10:30:56.376` | Full date and time (including milliseconds) |

Years of any length are supported, including BCE (Before Common Era) years, which should be specified with a negative sign:

```json
[
    {
        "event_label": "-509 BC, The founding of the Roman Empire",
        "show_event_label": true,
        "event_timestamp": "-509"
    },
    {
        "event_label": "15232, Simultaneous total solar eclipse and transit of Venus",
        "show_event_label": true,
        "event_timestamp": "15232-04-05"
    }
]
```