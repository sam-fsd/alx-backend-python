#!/usr/bin/env python3
"""defines a function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number by a specified
    multiplier.

    Parameters:
        multiplier (float): The multiplier to be used for
        multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float as
        input and returns the result of multiplying it by the
        specified multiplier.
    """
    def inner_multiplier(n: float) -> float:
        return multiplier * n

    return inner_multiplier
