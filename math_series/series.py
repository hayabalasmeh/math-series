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
    if first == 0 and second == 1:

        return [fibonacci(i) for i in range(n)]

    elif first == 2 and second == 1:
        return [lucas(i) for i in range(n)]

    else:
        return [fibonacci(i) for i in range(first, n)]


# def fibonacci_list(n):
    # for

    """
    fib(2)+ fib(1)fib(1)+ fib(0)
    0
    """
