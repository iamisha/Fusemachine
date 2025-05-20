import pandas as pd

L = {
    "COL1": [1, 2, 3, 4, 5],
    "COL2": ["A", "B", "A", "C", "B"],
    "COL3": [10, 20, 30, 40, 50],
}

df = pd.DataFrame(L)
print(df)

bool_index = (df["COL1"] > 3) | (df["COL2"] == "B")
print(bool_index)
print(df[bool_index])
