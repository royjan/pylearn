from functools import wraps


def memorize(function):
    cache = {}

    @wraps(function)
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        cache[args] = function(*args)
        print(f"{function.__name__}({args[0]})={cache[args]}")
        return cache[args]

    return decorated_function


@memorize
def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(9))
print(fib(10))
print(fib.__name__)
