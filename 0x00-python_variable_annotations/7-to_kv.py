#!/usr/bin/env python3
"""defines a function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a key (k) as a string and a value (v) as either an
    integer or a float.
    It returns a tuple containing the key (k) and the square of the value
    (v) as a float.

    Parameters:
    - k (str): The key as a string.
    - v (Union[int, float]): The value as either an integer or a float.

    Returns:
    - Tuple[str, float]: A tuple containing the key (k) and the square of
    the value (v) as a float.
    """
    return (k, v * v)
