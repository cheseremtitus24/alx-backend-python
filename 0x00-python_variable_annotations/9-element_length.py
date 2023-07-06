#!/usr/bin/env python3
"""
This module contains the str function that
returns the string representation of a float input
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Takes a Sequence of items which can be a list,dict or tuple
    and returns a list of tuples of the sequence paired with
    their respective lengths
    """
    return [(i, len(i)) for i in lst]
