from functools import wraps


def memoize(function):
    cache = {}

    # @wraps(function)
    def decorated_function(*args):
        number = args[0]
        if number in cache:
            return cache[number]
        cache[number] = function(*args)
        print(f"{function.__name__}({number})={cache[number]}")
        return cache[number]

    return decorated_function


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(9))
print(fib(10))
print(fib.__name__)
