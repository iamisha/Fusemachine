import pandas as pd

L = {
    "A": [1, 2, 3, 4],
    "B": [5, 6, 7, 8],
}
df = pd.DataFrame(L)
print(df)

df1 = df.apply(sum, axis=0)
print(df1)

df2 = df.apply(sum, axis=1)
print(df2)
