import pandas as pd
from scipy.stats import kurtosis,skew
import collections

data = pd.read_csv("dataset/Iris.csv")
data.drop(["Id"],inplace = True,axis=1)
print("\nDATA OVERVIEW :")
print(data.head())

print("\nSHAPE  :")
print(data.shape)
cols = data.columns[0:4]
print(cols)

print("\nCOUNT  :")
for c in cols:
    print(c,"\t",len(data[c]))

def findMean(data):
    sumation = sum(data)
    m = sumation/len(data)
    return m

def findMedian(data):
    n = len(data)
    try :
        data = data.tolist()
    except :
        pass
    data.sort()
    if(n/2==0):
        m1 = data[n//2]
        m2 = data[n//2-1]
        med = (m1+m2)/2
    else:
        med = data[n//2]
    return med


def findVariance(data):
    data.tolist()
    n = len(data)
    mean = findMean(data)
    variance = sum([((x - mean)**2) for x in data])/n
    return variance


def findStd(data):
    variance = findVariance(data)
    std = variance ** 0.5
    return std

def Q1(data):
    data = data.tolist()
    data.sort()
    mIndex = len(data)//2
    q1 = findMedian(data[:mIndex])
    return q1

def Q3(data):
    data = data.tolist()
    data.sort()
    mIndex = len(data)//2
    q3 = findMedian(data[mIndex:])
    return q3

def IQR(data):
    q3 = Q3(data)
    q1 = Q1(data)
    return q3-q1

def skewness(data):
    std = findStd(data)
    mean = findMean(data)
    median = findMedian(data)
    # data = data.tolist()
    # n = len(data)

    # sumation = sum([((x - mean)**3)for x in data])
    # skew = sumation /(n-1)* (std**3)
    skew = 3*(mean-median)/std
    return skew

def kurtosis(data):
    std = findStd(data)
    mean = findMean(data)
    data = data.tolist()
    n = len(data)
    sumation = sum([((x-mean)**4)for x in data])
    sumation2 = sum([((x-(mean**2))**2)for x in data])
    kurt = n*(sumation/sumation2)
    return kurt

print("\nMEAN : ")
for c in cols:
    print(c,"\t",findMean(data[c]))



print("\nMEDIAN : ")
for c in cols:
    print(c,"\t",findMedian(data[c]))


print("\nVARIANCE : ")
for c in cols:
    print(c,"\t",findVariance(data[c]))



print("\nSTANDARD DEVIATION : ")
for c in cols:
    print(c,"\t",findStd(data[c]))

print("\nQ1")
for c in cols:
    print(c,"\t",Q1(data[c]))

print("\nQ3")
for c in cols:
    print(c,"\t",Q3(data[c]))

print("\nIQR")
for c in cols:
    print(c,"\t",IQR(data[c]))

print("\nMAX : ")
for c in cols:
    print(c,"\t",max(data[c]))

print("\nMIN : ")
for c in cols:
    print(c,"\t",min(data[c]))

data_grp = data.groupby("Species")

print("\nKurtosis")
for c in cols:
    print(c,"\t",kurtosis(data[c]))

print("\nSkewness")
for c in cols:
    print(c,"\t",skewness(data[c]))
