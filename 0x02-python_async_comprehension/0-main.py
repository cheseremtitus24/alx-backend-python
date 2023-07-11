#!/usr/bin/env python3

import asyncio
import time

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)
res = time.perf_counter()
asyncio.run(print_yielded_values())
print("Total Exec time is ", time.perf_counter() - res)