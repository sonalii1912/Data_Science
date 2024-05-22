
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("dataset/movies.csv")
print("_______________________________________________________________________")
print("Dataframe:")
print(df)
print("_______________________________________________________________________")
print("NULL elements of each columns:")
print(df.isnull().sum())
print("_______________________________________________________________________")

# delete column 9 as it has 9539 null elements in 9999 obs.
df.pop("Gross")

# print("NULL GENRE:", df.loc[df["GENRE"] == "\0"])
df["YEAR"] = df["YEAR"].fillna(method='ffill')

# Fill "Not available" in place of empty genre
df["GENRE"] = df["GENRE"].fillna("Not available")

# Fill null ratings by mean of rating
df["RATING"] = df["RATING"].fillna(np.mean(df["RATING"]))

# Fill empty values of votes by 0
df["VOTES"] = df["VOTES"].fillna(0)

df.dropna(inplace=True)

# # Fill unknown runtime by mean of runtime
# df["RunTime"] = df["RunTime"].fillna(np.mean(df["RunTime"]))
print(df)
print("_______________________________________________________________________")
print(df.isnull().sum())
print("_______________________________________________________________________")


# Part B
plt.boxplot(df["RATING"])

plt.boxplot(df["RunTime"])
plt.show()
# print(df["VOTES"])
