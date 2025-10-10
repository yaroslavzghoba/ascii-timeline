import math
from typing import List
from model.event import Event
from model.timeline_label import TimelineLabel
from utils.constants import Constants
from utils.get_percentage import get_percentage
from utils.sort_events import sort_events
from utils.timeline_label_helpers import TimelineLabelHelpers
from utils.to_epoch_millis import to_epoch_millis


class AsciiTimeline:

    def generate(events: List[Event], length: int):
        """Generate a new timeline using ASCII characters."""

        # Return some placeholder if there are no events or length is too short.
        if len(events) == 0 or length in [0, 1]: 
            pointed_section_char = Constants.POINTED_TIMELINE_SECTION_CHAR
            unpointed_section_char = Constants.UNPOINTED_TIMELINE_SECTION_CHAR
            print((pointed_section_char if bool(len(events)) else unpointed_section_char) * length)
            return

        events = sort_events(events)
        # Define timeline range.
        earliest_timestamp, latest_timestamp = events[0].timestamp, events[-1].timestamp
        earliest_timestamp_epoch_millis = to_epoch_millis(earliest_timestamp)
        latest_timestamp_epoch_millis = to_epoch_millis(latest_timestamp)

        labels_to_place: List[TimelineLabel] = []
        for event in events:
            # Calculate position of each event on the timeline.
            event_epoch_millis = to_epoch_millis(event.timestamp)
            relativ_position = get_percentage(value=event_epoch_millis,
                                              min_value=earliest_timestamp_epoch_millis,
                                              max_value=latest_timestamp_epoch_millis)
            position_on_timeline = max(0, math.ceil(length * relativ_position) - 1)

            # Position the label relativ to oher labels on the timeline.
            # Other labels can be shifted up or down if necessary.
            label = f"{Constants.EVENT_LABEL_PREFIX}{event.label}{Constants.EVENT_LABEL_SUFFIX}"
            labels_to_place = AsciiTimeline.__add_label(label, position_on_timeline, labels_to_place)

        result = AsciiTimeline.__render_timeline(labels_to_place, length)
        print(result)


    def __render_timeline(labels: List[TimelineLabel], length: int) -> str:
        # TODO: Write a documentation for the method.

        labels = TimelineLabelHelpers.sort_labels_by_layer(labels, reverse=True)

        # Initialize empty timeline.
        timeline = [Constants.UNPOINTED_TIMELINE_SECTION_CHAR for _ in range(length)]  
        # Set event points on the timeline.
        for label in labels:
            timeline[label.start_offset] = Constants.POINTED_TIMELINE_SECTION_CHAR

        lines_to_print = []
        lowest_layer, highest_layer = min(0, labels[-1].layer), labels[0].layer
        # Add a event labels on each layer
        for layer in range(highest_layer, lowest_layer - 1, -1):
            # If this is the layer for the timeline.
            if layer == 0:
                lines_to_print.append("".join(timeline))
                continue

            # If this is the layer for the event labels.
            current_line = ""
            labels_on_layer = TimelineLabelHelpers.get_labels_on_layer(labels, layer)
            for label in labels_on_layer:
                current_line = TimelineLabelHelpers.print_label_on(label, current_line)
            lines_to_print.append(current_line)

        return "\n".join(lines_to_print)


    def __add_label(new_label: str, start_offset: int, labels: List[TimelineLabel]) -> List[TimelineLabel]:
        """
        Attempts to place a new label on the timeline while maintaining separation by layers.
        Labels with layer equals to 0 are ignored.
        """

        # Labels to be placed above
        labels_above = [label for label in labels if TimelineLabelHelpers.is_label_above(label)]
        labels_above = TimelineLabelHelpers.sort_labels_by_layer(labels_above)
        # Labels to be placed below
        labels_below = [label for label in labels if TimelineLabelHelpers.is_label_below(label)]
        labels_below = TimelineLabelHelpers.sort_labels_by_layer(labels_below, reverse=True)

        # Check space availability in the layer above.
        top_space = 0
        labels_on_layer_above = TimelineLabelHelpers.get_labels_on_layer(labels_above, layer=1)
        for label in labels_on_layer_above:
            top_space = max(top_space, label.start_offset + len(label.label))
        # Check space availability in the layer below.
        bottom_space = 0
        labels_on_layer_below = TimelineLabelHelpers.get_labels_on_layer(labels_below, layer=-1)
        for label in labels_on_layer_below:
            bottom_space = max(bottom_space, label.start_offset + len(label.label))

        new_label_layer = 0
        if top_space <= start_offset:
            # Place on the layer above, if there is space.
            new_label_layer = 1
        elif bottom_space <= start_offset:
            # Or place on the layer below, if there is space.
            new_label_layer = -1
        elif len(labels_above) > len(labels_below):
            # Or shift the layers below and place the label if there are enough labels above.
            labels_below = TimelineLabelHelpers.shift_layers(labels_below, -1)
            new_label_layer = -1
        else:
            # Otherwise, shift the layers above and place the label.
            labels_above = TimelineLabelHelpers.shift_layers(labels_above, +1)
            new_label_layer = 1

        return labels_below + labels_above + [TimelineLabel(new_label_layer, start_offset, new_label)]