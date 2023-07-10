#!/usr/bin/env python3
"""Returns an Asyncio Task of Generated Random Numbers


script requires built in random and asyncio module imports
and uses sleep and uniform from former and latter modules
respectively.

This file can also be imported as a module and contains
the following functions:
    * task_wait_random - returns an asyncio task of a list randomly generated float values

"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns an asyncio Task of Random Number After a Delay timer

    Parameters
    ----------
    n: int
        The number of times the the random generator function should be called
    max_delay : int
        The delay time interval (default is 10)

    Returns
    -------
    list
        a list of randomly generated floating point values sorted in Ascending order
    """

    # spawns wait_random function n-times with specified max_delay
    return sorted(await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n))
    ))
