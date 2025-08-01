#!/usr/bin/env python3
"""Module to measure average runtime of wait_n coroutine."""

import time
import asyncio
from typing import Union

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of wait_n(n, max_delay).

    Args:
        n (int): Number of concurrent wait_random calls.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        float: Average time per wait_random call in seconds.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    total_time = end - start
    return total_time / n
