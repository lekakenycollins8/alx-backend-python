#!/usr/bin/env python3
"""coroutine that takes in an integer and waits for random delay"""


import asyncio
import random


async def wait_random(max_delay=10):
    """awaits a random delay and eventually returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
