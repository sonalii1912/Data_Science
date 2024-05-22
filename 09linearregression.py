import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

while True:
  x=int(input("Enter 1 for applying Linear Regression model on attribute OutCome (0 to exit): "))
  if x==1:
    dia_df=pd.read_csv('dataset/diabetes.csv')
    dia_df
    dia_df.head()
    X= dia_df.drop(labels= 'Outcome', axis= 1)
    y= dia_df['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.1, random_state= 11)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr.predict(X_test)
    pred = lr.predict(X_test)
    print('Mean Absolute Error:', mean_absolute_error(y_test, pred))
    print('Mean Squared Error:', mean_squared_error(y_test, pred))
    print('Mean Root Squared Error:', np.sqrt(mean_squared_error(y_test, pred)))
    print('Actual Value : ', y.loc[8])
    print('Predicted Value : ', pred[8])
  else:
    print("Thank You!")
    break