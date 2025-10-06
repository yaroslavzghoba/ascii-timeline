from model.timeline_label import TimelineLabel
from typing import List
from dataclasses import replace
from utils.constants import Constants


class TimelineLabelHelpers:
    # TODO: Write a documentation for the class

    def sort_labels_by_layer(labels: List[TimelineLabel], reverse: bool = False) -> List[TimelineLabel]:
        """Sorts a list of timeline labels by the layer column in ascending chronological order."""
        return sorted(labels, key=lambda label: label.layer, reverse=reverse)
    

    def is_label_above(label: TimelineLabel) -> bool:
        return label.layer > 0
    

    def is_label_below(label: TimelineLabel) -> bool:
        return label.layer < 0
    

    def get_label_total_length(label: TimelineLabel) -> int:
        """Calculate the length from the beginning of the offset to the end of the label content."""
        return len(f"{' ' * label.start_offset}{label.label}")
    

    def shift_layers(labels: List[TimelineLabel], delta: int) -> List[TimelineLabel]:
        """Shift all label layers by a delta (positive or negative)."""
        return [label.replace_layer(label.layer + delta) for label in labels]
    

    def get_labels_on_layer(labels: List[TimelineLabel], layer: int) -> List[TimelineLabel]:
        return [label for label in labels if label.layer == layer]
    

    def print_label_on(label: TimelineLabel, source_line: str) -> str:
        label_total_length = label.start_offset + len(label.label)
        while len(source_line) < label_total_length:
            source_line += " "
        line = list(source_line)
        for index, char in enumerate(label.label):
            line[index + label.start_offset] = char
        return "".join(line)
    