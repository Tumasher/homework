import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_csv('emojis.csv')
d['Year'] = pd.to_datetime(d['Year'], format='%Y')
d_year = d.groupby(d['Year'].dt.year).size()
plt.figure(figsize=(10, 6))
d_year.plot(kind='line', color='red')
plt.title('Количество созданных эмоджи за каждый год')
plt.xlabel('Год')
plt.ylabel('Кол-во')
plt.show()