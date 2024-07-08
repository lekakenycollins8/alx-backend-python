#!/usr/bin/env python3
"""executes multiple coroutines at the same time"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait random n times with specified delay
    and returns list of delays"""
    delays: List[float] = []
    tasks: List[asyncio.Task] = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]

    results: List[float] = await asyncio.gather(*tasks)
    for result in results:
        delays.append(result)

    # insertion sort to sort the delays
    for i in range(1, len(delays)):
        current: float = delays[i]
        prev: int = i - 1
        while prev >= 0 and current < delays[prev]:
            delays[prev + 1] = delays[prev]
            prev -= 1
        delays[prev + 1] = current

    return delays
