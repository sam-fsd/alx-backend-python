#!/usr/bin/env python3
""" Define an annotated coroutine fn"""

from typing import Optional
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random amount of time and returns the delay.

    Parameters:
    - max_delay (Optional[int]): The maximum delay in seconds. Defaults to 10.

    Returns:
    - float: The random delay in seconds.

    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
