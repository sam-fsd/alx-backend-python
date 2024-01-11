#!/usr/bin/env python3
"""defines a function"""

from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing a mixture of integers and floats.

    Parameters:
    mxd_list (List[Union[int, float]]): A list containing a mixture of
    integers and floats.

    Returns:
    float: The sum of all the numbers in the list.

    Example:
    >>> sum_mixed_list([1, 2.5, 3, 4.75])
    11.25
    """
    sum: float = 0.0

    for num in mxd_list:
        sum += num

    return sum
