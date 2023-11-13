import math


def repeat(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result % 2 != 0:
            return fn(result)
        else:
            return result
    return wrapper


@repeat
def plus(a):
    return a + 1


print(plus(5), "\n")

@repeat
def minus(b):
    return b - 1


print(minus(10))