#!/usr/bin/env python3

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())
res = time.perf_counter()
asyncio.run(main())
print("Total Exec time is ", time.perf_counter() - res)