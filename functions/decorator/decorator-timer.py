import time
from functools import wraps


def timeit(function: callable):
    @wraps(function)
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(f"{function.__name__} took: {time.time() - start_time} seconds")
        return result

    return wrap


@timeit
def long_task():
    for _ in range(10_000_000):
        pass


if __name__ == '__main__':
    long_task()
    print(long_task.__name__)
