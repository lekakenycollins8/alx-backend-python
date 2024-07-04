#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list which takes a list
mxd_lst of ints and floats and returns their sum as a float."""


from typing import List, Union


numbers = Union[int, float]


def sum_mixed_list(mxd_lst: List[numbers]) -> float:
    """Return the sum of a list of integers and floats as a float."""
    return sum(mxd_lst)
