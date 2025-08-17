#!/usr/bin/env python3
"""
This module has a helper function for pagination
It returns start & end index based on page and page_size
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return tuple (start, end) index for pagination
    - page: current page number (starts from 1)
    - page_size: number of items per page
    """
    # Example: page=3, size=15 → start=30, end=45
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
