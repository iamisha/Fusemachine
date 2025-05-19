import pandas as pd

L = {
    "Company": ["Ford", "Chevy", "Toyota", "Honda", "Nissan"],
    "Color": ["Red", "Blue", "Green", "Yellow", "Black"],
    "Doors": [4, 2, 2, 4, 4],
}

df = pd.DataFrame(L)
print(df.iloc[:3, [0, 2]])
