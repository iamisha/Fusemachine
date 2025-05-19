import pandas as pd

# Create pandas DataFrame using a list
L = ["Ford", "Chevy", "Toyota", "Honda"]
df = pd.DataFrame(L)
print(df)

# Create pandas DataFrame using a dictionary
dict = {"Company": ["Ford", "Chevy", "Toyota", "Honda"], "Doors": [4, 2, 2, 4]}
df2 = pd.DataFrame(dict)
print(df2)

# Creating pandas dataframe using Series
s = pd.Series(L)
df3 = s.to_frame()
print(df3)
