import pandas as pd
import numpy as np

# Create pandas series using a list
L = ["Ford", "Chevy", "Toyota", "Honda"]
s = pd.Series(L)
# Create a pandas series using a list with custom index
# s = pd.Series(L, index=[1, 2, 3, 4])
print(s)

# Create a pandas Series using numpy array
arr = np.array(L)
s2 = pd.Series(arr)
print(s2)

# create a pandas Series using a dictionary
dict = {"a": 1, "b": 2, "c": 3}
s3 = pd.Series(dict)
print(s3)

# Accessing element of pandas Series
print(s[:2])  # Accessing first two elements
