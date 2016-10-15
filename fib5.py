
from functools import lru_cache
from call_counter import countcalls


@countcalls
@lru_cache(maxsize=1024)
def fib5(n):
    if n <= 2:
        return 1
    else:
        return fib5(n-1) + fib5(n-2)
