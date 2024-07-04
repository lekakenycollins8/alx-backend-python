#!/usr/bin/env python3
"""Duck-typing an iterable object"""

from typing import Iterable, List, Tuple, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing the length of each element and the element itself"""
    return [(i, len(i)) for i in lst]