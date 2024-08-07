#!/usr/bin/env python3
"""Type-annotated function safe_first_element"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return variable of Any type"""
    if lst:
        return lst[0]
    else:
        return None
