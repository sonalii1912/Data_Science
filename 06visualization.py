import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("dataset/diabetes.csv")

col = data.columns
print(data.head())
print(data.info())

fig = plt.figure()
plt.title("Glucose")
plt.plot(data["Glucose"])

fig = plt.figure()
plt.title("Age vs BMI")
plt.xlabel("Age")
plt.ylabel("BMI")
plt.scatter(data["Age"],data["BMI"])

data.hist(figsize=(8,6))

plt.figure()
plt.title("Results")
plt.xlabel("Outcome")
plt.ylabel("No.of People")
data["Outcome"].value_counts().plot(kind='bar')

plt.figure()
plt.title("Outcome in Pie Chart")
data["Outcome"].value_counts().plot(kind='pie')

fig = plt.figure()
hm = sns.heatmap(data=data)

fig = plt.figure()
corr = data.corr()
sns.heatmap(corr)
plt.show()
