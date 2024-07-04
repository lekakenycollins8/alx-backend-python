#!/usr/bin/env python3
"""Type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier."""

from typing import Callable

multiplierFunction = Callable[[float], float]

def make_multiplier(multiplier: float) -> multiplierFunction:
    """Return a function that multiplies a float by multiplier."""
    def multiply(n: float) -> float:
        """Return the product of a float multiplied by multiplier."""
        return n * multiplier
    return multiply