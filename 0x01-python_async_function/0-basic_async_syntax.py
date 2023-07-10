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
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Returns a Random Number After a Delay timer

    Parameters
    ----------
    max_delay : int
        The delay time interval (default is 10)

    Returns
    -------
    float
        a randomly generated floating point value
    """

    await asyncio.sleep(max_delay)
    return random.uniform(0, 10)
