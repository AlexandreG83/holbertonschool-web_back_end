#!/usr/bin/env python3
"""
Execute multiple tasks concurrently.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Spawn task_wait_random n times and
    return the delays in ascending order.
    """
    tasks = asyncio.create_task(wait_random(max_delay))
    return tasks
