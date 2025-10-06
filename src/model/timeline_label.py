from dataclasses import dataclass, field

@dataclass
class TimelineLabel:
    """
    An event label that can be plased on timeline.
    
    Attributes
    ----------
    __layer : int
        The timeline layer where the label should be displayed (for visual separation).
    start_offset : int
        The starting time offset relative to the beginning of the timeline.
    label : str
        The textual description of the event.
    """
    __layer: int = field(init=True, repr=False)
    start_offset: int
    label: str

    def __post_init__(self):
        if self.__layer == 0:
            raise ValueError(f"The label cannot be placed on the layer 0.")


    @property
    def layer(self) -> int:
        return self.__layer
    

    @layer.setter
    def layer(self, value: int):
        if value == 0:
            raise ValueError("The label cannot be placed on the layer 0.")
        self.__layer = value

    
    def replace_layer(self, layer: int):
        return TimelineLabel(layer, self.start_offset, self.label)
