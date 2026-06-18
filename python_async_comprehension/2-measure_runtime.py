#!/usr/bin/env python3
"""
Module that measures the runtime of async comprehensions.
"""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """
    Execute four async comprehensions in parallel
    and return the total execution time.
    """
    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.time()

    return end - start