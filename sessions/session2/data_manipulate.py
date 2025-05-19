import pandas as pd

L = {
    "Company": ["Ford", "Chevy", None, "Honda", "Nissan"],
    "Color": ["Red", "Blue", "Green", "Yellow", None],
    "Doors": [4, 2, 2, None, 4],
}

df = pd.DataFrame(L)
print("Before change:\n", df)

# Single element change
# df.loc[0, 'Color'] = 'Pink'
# print("After change:\n", df)

# Fill NaN values with a specific value
# df.fillna('a', inplace=True)
# print("After fillna:\n", df)

# drop rows with NaN values
df.dropna(axis=0, inplace=True)
print("After dropna:\n", df)

# drop columns with NaN values
# df.dropna(axis=1, inplace=True)
# print("After dropna:\n", df)
