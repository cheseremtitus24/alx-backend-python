#!/usr/bin/env python3
""" Uses List Comprehension to Call an Asynchronous Generator Function

This implementation is 2x faster than an equivalent implementation as an
asynchronous iterator according to PEP 525.

script requires built in asyncio module, typing.List[for versions above 3.8 use list[float]] imports

This file can also be imported as a module and contains
the following functions:
    * async_generator - is a generator function that yields floating point random numbers
    * async_comprehension - is an async function that calls async_generator through List Comprehension

"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Implements List Comprehension that executes an Async Function that returns Floating point Values

    Returns
    -------
    List 
        a list randomly generated floating point values
    """
    retval: List[float] = list()
    retval = [i async for i in async_generator()]

    return retval
