#!/usr/bin/env python3
"""
This module contains variable annotations
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    info: type annotation for python version 3.8 & below
    you must import List from typing module
    for versions above just use list[float]
    sum_list: returns summation of a list of floats
    input_list: list of floats
    returns: float
    """
    return sum(input_list)
