#!/usr/bin/env python3
"""Module containing a function that creates a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier."""
    def multiply(value: float) -> float:
        """Return the product of a float and the multiplier."""
        return value * multiplier

    return multiply
