#!/usr/bin/env python3
"""defines a function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of all elements in a given list.

    Parameters:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all elements in the input list.

    Example:
        >>> sum_list([1.5, 2.5, 3.5])
        7.5
    """
    sum: float = 0.0

    for num in input_list:
        sum += num

    return sum
