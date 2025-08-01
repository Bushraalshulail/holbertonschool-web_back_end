#!/usr/bin/env python3
"""Module that contains a function to return a tuple of a string
and the square of a number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where the first element is a string,
    and the second is the square of an int or float as a float."""
    return (k, float(v ** 2))
