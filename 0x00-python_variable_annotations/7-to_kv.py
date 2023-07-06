#!/usr/bin/env python3
"""
This module contains the to_kv function that
creates a key value pair of an input string key
and an input value that is squared.
"""
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv: returns a key value pair of squared value input
    str1: str
    str2: int or float
    returns: tuple(str,float)
    """
    return (k, v**2)
