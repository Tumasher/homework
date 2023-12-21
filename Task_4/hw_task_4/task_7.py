import numpy as np


def func(A, S, last=False):
    B = np.random.rand(S, len(A))
    Prod = np.dot(A, B)
    S = np.sum(Prod, axis=1)
    if not last:
        S = np.sin(S)
    else:
        S = np.maximum(S, 0)
    return S, B


S1, B1 = func(np.random.rand(5), 10)
S2, B2 = func(S1, 10)
S3, B3 = func(S2, 5, last=True)