#!/usr/bin/env python3
"""executes multiple coroutines at the same time"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """spawns wait random n times with specified delay
    and returns list of delays"""
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    results = await asyncio.gather(*tasks)
    for result in results:
        delays.append(result)

    # insertion sort to sort the delays
    for i in range(1, len(delays)):
        current = delays[i]
        prev = i - 1
        while prev >= 0 and current < delays[prev]:
            delays[prev + 1] = delays[prev]
            prev -= 1
        delays[prev + 1] = current

    return delays
