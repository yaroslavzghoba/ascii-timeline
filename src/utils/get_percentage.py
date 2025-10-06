def get_percentage(value: int, min_value: int, max_value: int) -> float:
    """
    Calculates the position of the passed value as a percentage of the range [min_value, max_value].
    

    Parameters
    ----------
    value : int
        The value that should be represented as a percentage of the range [min_value, max_value].
    min_value : int
        The minimum possible value of the range.
    max_value : int
        The maximum possible value of the range.

    Returns
    -------
    Fractional percentage value in the range [0.0, 1.0]. 
    For example, with input values of 2, 1, 5, the function will return 0.25, 
    because 0.25 is the relative position of 2 in the range [1, 5].
    """

    range_size = max_value - min_value
    if range_size == 0:
        return 0.0 if value <= min_value else 1.0

    distance_from_min = value - min_value
    percentage = distance_from_min / range_size
    return percentage