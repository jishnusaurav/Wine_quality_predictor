import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
dataset = pd.read_csv('/home/jishnu/Desktop/winequality-red.csv')
print("Welcome!!!")
print("Enter the following values to get the quality of your Red Wine")
X = dataset[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates','alcohol']].values
y = dataset['quality'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

fixed_acidity=float(input("Enter the fixed acidity content:"))
volatile_acidity=float(input("Enter the volatale acidity content:"))
citric_acid=float(input("Enter the citric acid content:"))
residual_sugar=float(input("Enter the residual sugar content:"))
chlorides=float(input("Enter the chlorides content:"))
free_sulphur_dioxide=float(input("Enter the free sulphur dioxide:"))
total_sulphur_dioxide=float(input("Enter the total sulphur dioxide:"))
density=float(input("Enter the density of the Wine:"))
ph=float(input("Enter the pH:"))
sulphates=float(input("Enter the sulphates content:"))
alcohol=float(input("Enter the alcohol content:"))





list1=[[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulphur_dioxide,total_sulphur_dioxide,density,ph,sulphates,alcohol]]

print("")
print("")
print("")

print("The quality of your wine is :")

y_pred = regressor.predict(list1)
for i in y_pred:
	print(i)




