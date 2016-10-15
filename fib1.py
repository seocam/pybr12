
from call_counter import countcalls

@countcalls
def fib1(n):
    if n <= 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)
