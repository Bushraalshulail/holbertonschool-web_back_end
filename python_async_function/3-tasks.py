#!/usr/bin/env python3
"""Module to create asyncio.Task from wait_random coroutine."""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task from wait_random coroutine with max_delay.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: The created asyncio task.
    """
    return asyncio.create_task(wait_random(max_delay))
