import pandas as pd

L = {
    "gender": ["f", "m", "m", "f", "m", "f", "m"],
    "weight": [56, 60, 59, 55, 65, 52, 61],
}

df = pd.DataFrame(L)
print(df)

# Aggregation functions
# min, max, mean, sum

print(df.groupby("gender").agg(["min", "max", "mean", "sum"]))

# simple grouping with Single aggregation
print(df.groupby("gender")["weight"].mean())

# multiple aggregation
print(df.groupby("gender")["weight"].agg(["mean", "max", "min"]))


# custom aggregation fun
def custom_agg(x):
    return x.max() - x.min()


print(df.groupby("gender")["weight"].agg(custom_agg))

# Named Aggregations(Cleaner Syntax)
print(
    df.groupby("gender").agg(
        avg_weight=("weight", "mean"), age_range=("weight", lambda x: x.max() - x.min())
    )
)

# Filter after groupby
print(df.groupby("gender").filter(lambda x: x["weight"].sum() > 200))
