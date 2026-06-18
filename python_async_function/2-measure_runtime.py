#!/usr/bin/env python3
"""
Measure the runtime of four parallel async comprehensions.
"""

import asyncio
import time

async_comprehension = __import__(
    '1-concurrent_coroutines'
).async_comprehension


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Execute four async comprehensions concurrently
    and return the total runtime.
    """
    start = time.time()
    asyncio.run(async_comprehension(n, max_delay))

    end = time.time()
    final = (end - start) / n
    return final
