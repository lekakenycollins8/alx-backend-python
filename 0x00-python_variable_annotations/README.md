# Python Type Annotations and Type Checking

## Overview

This document provides an overview of type annotations, duck typing, and type checking using mypy in Python. It also covers the use of `TypeVar` for creating generic types.

## Type Annotations in Python

Type annotations in Python help specify the expected types of variables, function parameters, and return values. They enhance code readability and allow for type checking with tools like `mypy`.

### Function Signatures and Variable Types

You can specify function signatures and variable types using type annotations from the `typing` module.

```python
from typing import List, Tuple, Union

def process_numbers(numbers: List[Union[int, float]]) -> float:
    total: float = sum(numbers)
    return total
