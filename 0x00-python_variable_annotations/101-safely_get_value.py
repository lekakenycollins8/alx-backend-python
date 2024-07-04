#!/usr/bin/env python3
"""Function Annotation using TypeVar"""


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Function that returns the value of a key safely"""
    if key in dct:
        return dct[key]
    else:
        return default
