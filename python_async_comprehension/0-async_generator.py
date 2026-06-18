#!/usr/bin/env python3
"""
Create an asynchronous generator.
"""

from random import uniform
from typing import Generator
from asyncio import sleep

async def async_generator() -> Generator[float, None, None]:
    """
    Generate random numbers asynchronously.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)