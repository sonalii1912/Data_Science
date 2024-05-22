import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

data = pd.read_csv("dataset/Iris.csv")
data.drop(["Id"],inplace = True,axis=1)
print(data.head())

col = data.columns[0:4]

for c in col:
    fig = plt.figure()
    plt.title("Histogram of "+c)
    plt.ylabel("Frequency")
    plt.xlabel(c)
    plt.hist(data[c])


fig = plt.figure(figsize=(8,8))
fig.suptitle("Outlier Detection")

ax1 = fig.add_subplot(2,2,1)
ax1.boxplot(data["SepalLengthCm"])
ax1.title.set_text(col[0])

ax2 = fig.add_subplot(2,2,2)
ax2.boxplot(data["SepalWidthCm"])
ax2.title.set_text(col[1])

ax3 = fig.add_subplot(2,2,3)
ax3.boxplot(data["PetalLengthCm"])
ax3.title.set_text(col[2])

ax4 = fig.add_subplot(2,2,4)
ax4.boxplot(data["PetalWidthCm"])
ax4.title.set_text(col[3])

plt.show()