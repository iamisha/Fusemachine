import pandas as pd

# Create a simple DataFrame
data = {"Age": [18, 18, 22, 23, 24, 25], "Score": [60, 88, 92, 95, 85, 90]}

df = pd.DataFrame(data)

# # first 5 rows
# print(df.head())

# # last 5 rows
# print(df.tail())

# # Use describe() to get summary stats
# print(df.describe())

# use nunique() to get number of unique values in each column
print(df.nunique())

# use unique() to get unique values in a column
print(df["Age"].unique())

print(df["Age"].value_counts())

# Writing DataFrame to Disc
df.to_csv("file1.csv", index=False)
