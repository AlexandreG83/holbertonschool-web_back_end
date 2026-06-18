#!/usr/bin/env python3
"""
Basic asynchronous coroutine.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds
    and return the delay.
    async def → creates a coroutine.
    max_delay is an integer with a default value of 10.
    -> float indicates that the function returns a floating-point number.
    delay: generates a random real number between 0 and max_delay
    asyncio.sleep(delay): releases the event loop to run other coroutines.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
