import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import random

while True:
  x=int(input("Enter 1 for GaussianNB \nEnter 2 for Exit: "))
  if x==1:
    df=pd.read_csv('dataset/diabetes.csv')
    print(df.head())
    x=df.drop(labels='Outcome', axis=1)
    y=df.Outcome
    print(x.head())
    print("Shape of x",x.shape)
    print(y.head())
    print("Shape of y",y.shape)
    t= (float(input("Enter value for test size: ")))/100
    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=t,random_state=random.randrange(0,100))
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred = gnb.predict(X_test)
    print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

  else:
    print("Thank You!")
    break