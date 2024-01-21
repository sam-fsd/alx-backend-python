#!/usr/bin/env python3
"""  Module define an async comprehension coroutine.  """


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """  Async comprehension coroutine.  """
    return [i async for i in async_generator()]
