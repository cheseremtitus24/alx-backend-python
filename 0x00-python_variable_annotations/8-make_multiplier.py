#!/usr/bin/env python3
"""
Module features a type annotated function make_multiplier
other functions that fall under the representation of
typing.Callable are:
basic functions,lambdas, methods & classes
"""


from typing import Callable
# above import is deprecated in python 3.11  & you should use:
# from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier: make_multipliers two passed in parameters and returns their sum
    multiplier: float
    returns: a function(input:float) return a float(input*input)
    """
    def fun(multiplier: float) -> float:
        """
        input: float
        returns the square of multiplier
        """
        return float(multiplier * multiplier)
    return fun
