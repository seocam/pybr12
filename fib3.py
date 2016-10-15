
fib_dict = {1: 1, 2: 1}


def fib3(n):
    if n <= 2:
        return 1

    if n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fib3(n-1) + fib3(n-2)

    return fib_dict[n]
