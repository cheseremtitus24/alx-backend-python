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
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Timer function to Measure Execution of an Async function

    Parameters
    ----------
    n: int
        The number of times the the random generator function should be called
    max_delay : int
        The delay time interval

    Returns
    -------
    float
        The time elapsed during async function run
    """

    # setup the timer function
    timer: float = time.perf_counter()

    # call the async function to be timed
    asyncio.run(wait_n(n, max_delay))

    timer = time.perf_counter() - timer

    return timer
