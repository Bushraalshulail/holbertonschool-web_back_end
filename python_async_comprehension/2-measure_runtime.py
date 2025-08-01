#!/usr/bin/env python3
"""Coroutine that measures total runtime of running
async_comprehension 4 times in parallel"""

import asyncio
import time
from typing import Callable

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures total runtime of running
    async_comprehension 4 times in parallel"""
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    total_time = time.perf_counter() - start_time
    return total_time
