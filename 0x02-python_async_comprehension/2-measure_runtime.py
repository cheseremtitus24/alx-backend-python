#!/usr/bin/env python3
"""Measures the Performance of a Generator Function Executed in Parallel with asyncio.gather

Gather ensures that all the results are returned together and if it takes the length of time longest worker task 

script requires built in asyncio and time module imports

This file can also be imported as a module and contains
the following functions:
    * async_comprehension- is a generator function that yields number sequences
    * measure_runtime- function that measures the performance of an async function


"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the Execution Time of an Async Function

    Returns
    -------
    float
        elapsed time as floating point value
    """
    parallel_runs: int = 4
    runtime: float = time.perf_counter()
    await asyncio.gather(
        *(async_comprehension() for _ in range(parallel_runs)))
    return (time.perf_counter() - runtime)
