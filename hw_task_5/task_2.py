import pandas as pd
import numpy as np

d = pd.DataFrame(np.random.randint(1, 11, size=(10, 10)))

d.index = list("ABCDEFGHIJ")
my_row = d[d.apply(lambda row: all(row > 5), axis=1)]
if not my_row.empty:
    print("my_row:")
    print(my_row.iloc[0])
else:
    print("error")