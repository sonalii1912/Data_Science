from scipy.stats import ttest_1samp
from statsmodels.stats import weightstats as stests
from statsmodels.stats.weightstats import ztest as ztest
import scipy.stats as stats
import numpy as np
import pandas as pd
import statistics
x=0
while x<5:
  x=int(input("Enter 1 for ztest on PetalLengthCm\n Enter 2 for Exit: "))
  if x==1:
    df = pd.read_csv("dataset/IRIS.csv")
    print("IRIS Dataset: \n",df)
    df_sample=df.sample(75)
    print("Sample dataset with only 75 observations: \n", df_sample)
    df_sample_pl=df_sample.PetalLengthCm
    print("dataset sample with only petal length: \n", df_sample_pl)
    print("SAmple Description\n")
    print(df_sample_pl.describe())
    df_pl=df.PetalLengthCm
    print("dataset population with only petal length: \n", df_pl)
    print("Population description\n")
    print(df_pl.describe())
    print("Mean of population: ",statistics.mean(df_pl))
    ztest_Score, p_value= ztest(df_sample_pl,value = statistics.mean(df_pl) )
    print("ztest_score is: ", ztest_Score)
    print("p_value is: ",p_value)
    if p_value <0.05:
      print("we reject null hypothesis")
    else:
      print("we accept null hypothesis")
  else:
    print("Thank You!")
    break