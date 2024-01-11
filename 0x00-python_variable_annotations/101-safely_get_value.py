#!/usr/bin/env python3
"""defines an annotated function"""

from typing import Optional, Union, Any, TypeVar, Mapping


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Optional[Union[T, None]] = None) -> Union[Any, T]:
    """
    Return the value associated with the given key in the dictionary,
    or the default
    value if the key is not present.

    Parameters:
        dct (Mapping): The dictionary to search for the key.
        key (Any): The key to search for in the dictionary.
        default (Optional[Union[Any, None]]): The value to return
        if the key is notpresent in the dictionary. Defaults to None.

    Returns:
        Any: The value associated with the key in the dictionary, or
        the default value if the key is not present.

    """
    if key in dct:
        return dct[key]
    else:
        return default
