import pandas as pd
import numpy as np

d = pd.DataFrame(np.random.rand(10, 10))
d.index = list("ABCDEFGHIJ")
d.columns = list("abcdefghij")
print(f"\nРазмерность матрицы: {d.shape}")
print(f"\nИндексы столбцов: {d.columns}")
print(f"\nСреднее значение матрицы: {d.values.mean()}")
d.to_csv("matrix.csv", index=False)
print("\nМатрица записана в файл 'matrix.csv'")