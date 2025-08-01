#!/usr/bin/env python3
"""Module to run multiple wait_random coroutines concurrently and
return sorted delays."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay and
    return the list of delays in ascending order.

    Args:
        n (int): Number of times to run wait_random concurrently.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        List[float]: List of delay times in ascending order.
    """
    # Create tasks for concurrent execution
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays = []
    # Gather results in order of completion to maintain ascending order
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)

    return delays
