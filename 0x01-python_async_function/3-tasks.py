#!/usr/bin/env python3
"""Returns an Asyncio Task

Script creates an async task then returns it

script requires built in random and asyncio module imports
and uses sleep and uniform from former and latter modules
respectively.

This file can also be imported as a module and contains
the following functions:
    * wait_random - returns a randomly generated float value
    * task_wait_random - returns an Async Task

"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an Asynchronous Task created from asyncio.create_task(coro)

    Parameters
    ----------
    max_delay : int
        The delay time interval (default is 10)

    Returns
    -------
    asyncio.Task
        a callable task than can be run by an asyncio runnable
    """

    return asyncio.create_task(wait_random(max_delay))
