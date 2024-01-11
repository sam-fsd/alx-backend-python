#!/usr/bin/env python3
"""defines an annotated funtion"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array by repeating each element a specified
    number of times.

    Parameters:
    - lst (Tuple): The input array to be zoomed in.
    - factor (int): The number of times each element should be
    repeated. Default is 2.

    Returns:
    - List: The zoomed in array, with each element repeated
    'factor' times.

    Example:
    >>> zoom_array((1, 2, 3), 3)
    [1, 1, 1, 2, 2, 2, 3, 3, 3]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


tple = (12, 72, 91)

zoom_2x = zoom_array(tple)

zoom_3x = zoom_array(tple, 3)
