import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r'house-prices.csv')
print(df.head(10))

df = df.dropna()

x = df.drop(['Price'],axis=1)
x = pd.get_dummies(x, drop_first=True)
y = df['Price']

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=42)

lr = LinearRegression()
lr.fit(xtrain, ytrain)

ypred = lr.predict(xtest)

lrResults = xtest.copy()
lrResults['Actual Price'] = ytest
lrResults['Predicted Price'] = ypred
mse = mean_squared_error(ytest,ypred)
print(lrResults.head())
print("rmse: ",np.sqrt(mse))
