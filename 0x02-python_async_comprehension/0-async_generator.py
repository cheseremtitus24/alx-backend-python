#!/usr/bin/env python3
"""Generates a Random Number Using Asynchronous + Generator Function

This implementation is 2x faster than an equivalent implementation as an
asynchronous iterator according to PEP 525.

script requires built in asyncio module, typing.AsyncGenerator and random module imports
and uses asynchronous non-blocking sleep to mimic a producer function/subroutine.

This file can also be imported as a module and contains
the following functions:
    * async_generator - is a generator function that yields floating point random numbers


"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generates Random number Sequences between 0 and 10

    Returns
    -------
    float
        a randomly generated floating point value
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(.5)
