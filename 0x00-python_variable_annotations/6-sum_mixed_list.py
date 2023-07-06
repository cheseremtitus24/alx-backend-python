#!/usr/bin/env python3
"""
This module contains variable annotation
of a list with a mix of int & float
if python >= 3.8:
    mxd_list: list[float|int]
if python < 3.8:
    from typing import List, Union
    mxd_list: List[Union[float,int]]

"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    info: type annotation for python version 3.8 & below
    you must import List from typing module
    for versions above just use list[float]
    sum_mixed_list: returns summation of a list of floats
    input_list: list of floats
    returns: float
    """
    return sum(mxd_lst)
