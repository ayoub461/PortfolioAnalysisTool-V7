import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['row1', 'row2', 'row3'])

# Display all index row names
x = df.index[df['A']==1].tolist()
#print(df.index.asof_locs(df = 2))
print(x)