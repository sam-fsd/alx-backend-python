#!/usr/bin/env python3
"""defines a function"""

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of sequences as input and returns a list of
    tuples. Each tuple contains a sequence from the input list and its
    corresponding length.

    Parameters:
    - lst (Iterable[Sequence]): A list of sequences.

    Returns:
    - List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
    a sequence from the input list and its length.

    Example:
    >>> element_length(['abc', 'defg', 'hijkl'])
    [('abc', 3), ('defg', 4), ('hijkl', 5)]
    """
    return [(i, len(i)) for i in lst]
