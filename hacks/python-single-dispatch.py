from typing import Any
from functools import singledispatch

import numpy as np


# def multiply_each_number_naive(array: Any, number: int | float):
#     if type(array) is list:
#         return [item * number for item in array]
#     elif type(array) is np.ndarray:
#         return array * number
#     raise TypeError(f"unknown type: {type(array)}")


@singledispatch
def multiply_each_number(array: Any, _: int | float):
    raise TypeError(f"unknown type: {type(array)}")


@multiply_each_number.register
def _(array: list, number: int | float) -> list:
    return [item * number for item in array]


@multiply_each_number.register
def _(array: np.ndarray, number: int | float) -> np.ndarray:
    return array * number


if __name__ == '__main__':
    print(multiply_each_number([8, 2, 3], 4))  # [32, 8, 12]
    print(multiply_each_number(np.asarray([8, 2, 3]), 4))  # [32  8 12]
    print(multiply_each_number("something", 4))  # TypeError: unknown type: <class 'str'>
