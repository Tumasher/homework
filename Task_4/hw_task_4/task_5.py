import numpy as np


def matr(num):
    check = [i for i in range(2, num) if num % i == 0]

    if not check:
        print("Error")
        return

    for div1 in check:
        div2 = num // div1
        if div1 == 1 or div2 == 1:
            continue
        size = (div1, div2)
        m = np.random.rand(*size)
        print(f"Матрица {size}:")
        print(m)


matr(6)
matr(3)