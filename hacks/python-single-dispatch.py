from typing import Any
from functools import singledispatch

import numpy as np


@singledispatch
def multiply_each_number(array: Any, _: int | float) -> None:
    raise TypeError(f"unknown type: {type(array)}")


@multiply_each_number.register
def _(array: list, number: int | float) -> list:
    return [item * number for item in array]


@multiply_each_number.register
def _(array: np.ndarray, number: int | float) -> np.ndarray:
    return array * number


if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    np_array = np.array(lst)

    print(multiply_each_number(lst, 5))
    print(multiply_each_number(np_array, 5))
    print(multiply_each_number(12, 5))
