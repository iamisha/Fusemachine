import pandas as pd

L = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
}
df = pd.DataFrame(L)
print(df)

print(df[df["Name"].isin(["Alice", "Eve"])])
