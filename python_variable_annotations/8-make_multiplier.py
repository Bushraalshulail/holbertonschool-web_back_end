#!/usr/bin/env python3
"""Module that returns a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    def multiply(x: float) -> float:
        """Multiplies a float by the preset multiplier."""
        return x * multiplier

    return multiply
