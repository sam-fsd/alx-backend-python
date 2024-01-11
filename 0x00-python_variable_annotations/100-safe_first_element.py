#!/usr/bin/env python3
"""defines an annotated function"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence if it exists, otherwise
    return None.

    Parameters:
        lst (Sequence[Any]): The sequence from which to retrieve
        the first element.

    Returns:
        Union[Any, None]: The first element of the sequence if it
        exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
