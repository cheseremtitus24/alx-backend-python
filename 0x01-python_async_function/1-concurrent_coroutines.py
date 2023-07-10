#!/usr/bin/env python3
"""Returns a Random Number After a Delay timer

Script uses asynchronous programming to generate random
float values that are returned to the calling function

script requires built in random and asyncio module imports
and uses sleep and uniform from former and latter modules
respectively.

This file can also be imported as a module and contains
the following functions:
    * wait_random - returns a randomly generated float value

"""
import asyncio


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Returns a Random Number After a Delay timer

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
    wait_random = __import__('0-basic_async_syntax').wait_random

    # spawns wait_random function n-times with specified max_delay
    return sorted(await asyncio.gather(
        *(wait_random(max_delay) for i in range(n))
    ))
