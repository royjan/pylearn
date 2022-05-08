from time import time
from functools import wraps
from typing import Dict, List
from collections import defaultdict


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.4f sec' % (f.__name__, te - ts))
        return result

    return wrap


@timing
def naive_search(given_list: [int], give_number: int) -> bool:
    for number in given_list:
        if give_number == number:
            return True
    return False


def my_custom_hash(num: int) -> int:
    return num % 5


def my_custom_hash_bigger_number(num: int) -> int:
    return num % 100_000_000


@timing
def using_hash(given_datastruct: Dict[int, List[int]], given_item: int):
    hash_calculate = my_custom_hash(given_item)
    my_smaller_search = given_datastruct[hash_calculate]
    for item in my_smaller_search:
        if item == given_item:
            return True
    return False


#
# def save_graph():
#     from matplotlib import pyplot as plt
#     plt.bar(["1", "5", "N"], [2.1908, 0.5131, 0.000])
#     plt.xlabel("םילסה רפסמ")
#     plt.ylabel("הציר ןמז")
#     plt.savefig("graph.png")


if __name__ == '__main__':
    last_number = 100_000_000
    some_given_list = list(range(last_number + 1))
    number = -1

    print(naive_search(some_given_list, number))

    data_structure = defaultdict(list)
    for item in some_given_list:
        data_structure[my_custom_hash(item)].append(item)

    print(using_hash(data_structure, number))

    data_structure = defaultdict(list)
    for item in some_given_list:
        data_structure[my_custom_hash_bigger_number(item)].append(item)

    print(using_hash(data_structure, number))
