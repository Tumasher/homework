import pandas as pd

d = pd.read_csv('emojis.csv')
sort = d.sort_values(by='Rank', ascending=True)
print("Sorted:")
print(sort.head())
print(sort['Subcategory'].iloc[0])