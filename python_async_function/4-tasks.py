#!/usr/bin/env python3
"""Module to run multiple task_wait_random coroutines
concurrently and return sorted delays."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay and
    return the list of delays in ascending order.

    Args:
        n (int): Number of concurrent task_wait_random calls.
        max_delay (int): Maximum delay for each call.

    Returns:
        List[float]: List of delay times in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)

    return delays
