import pandas as pd

L = ["cat", "dog", "bird"]
df = pd.Series(L)
print(f"Before mapping:\n{df}")

animal_map = {"cat": "feline", "dog": "canine", "bird": "avian"}
df_mapped = df.map(animal_map)
print(f"After mapping:\n{df_mapped}")

L = [0, 1, 2, 3, 4, 5]
df = pd.Series(L)
print(f"Before mapping:\n{df}")

s = df.map(lambda x: x**2)
print(f"After mapping:\n{s}")
