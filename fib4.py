
from call_counter import countcalls


def memoize(func):
    cache = {}

    def decorator(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    decorator.cache = cache
    return decorator


@countcalls
@memoize
def fib4(n):
    if n <= 2:
        return 1
    else:
        return fib4(n-1) + fib4(n-2)
