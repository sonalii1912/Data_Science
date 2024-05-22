import pandas as pd
import numpy as np

print("______________________________________________________________________________")
df = pd.read_csv("sy.csv")
print(df)
print("______________________________________________________________________________")
print("Null values in original dataset:")
print(df.isnull().sum())
print("______________________________________________________________________________")

df.pop("Details_certification")
df.pop("Score_of_Online_certification")

# print(df["MHT_CET_Score"])
df["MHT_CET_Score"].replace("98.3℅ile", "98.3")
df["MHT_CET_Score"].replace("92.08 %ile", "92.08")
df["MHT_CET_Score"].replace("91%", "91.0")
df["MHT_CET_Score"].replace("80.8 percentile ", "80.8")

# print(df["MHT_CET_Score"])
# df["MHT_CET_Score"] = df["MHT_CET_Score"].fillna(df["MHT_CET_Score"].mean())
df["MHT_CET_Score"] = df["MHT_CET_Score"].fillna(96)
df["JEE_Main_score"] = df["JEE_Main_score"].fillna(90)
# j = {'None': 90, 'NON': 90, '-': 90, '70 percentile': 70}
# df["JEE_Main_Score"] = [j[item] for item in df["JEE_Main_Score"]]
# df["JEE_Main_score"] = df["JEE_Main_score"].fi
df["stars_hackerrank"] = df["stars_hackerrank"].fillna(0)
df["stars_codechef"] = df["stars_codechef"].fillna(0)
df["No_of_success_problems_codechef"] = df["No_of_success_problems_codechef"].fillna(0)
df["No_of_success_problems_hackerrank"] = df["No_of_success_problems_hackerrank"].fillna(0)
df.pop("No_of_success_problems_leetcode")

print("Null values in cleaned dataset:")
print(df.isnull().sum())

print("______________________________________________________________________________")
print("Cleaned dataset: ")
print(df)

# print(df["JEE_Main_score"])