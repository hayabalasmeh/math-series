def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n-1) + lucas(n-2))


def sum_series(n, first=0, second=1):
    # if first == 0 and second == 1:

    #     return [fibonacci(i) for i in range(n)]

    # elif first == 2 and second == 1:
    #     return [lucas(i) for i in range(n)]
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return (sum_series(n-1, first, second) + sum_series(n-2, first, second))


def sum_series_list(n, first=0, second=1):
    return [sum_series(i, first, second) for i in range(n)]

    """
    fib(2)+ fib(1)fib(1)+ fib(0)
    0
    """
