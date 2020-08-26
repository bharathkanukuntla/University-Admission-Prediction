# -*- coding: utf-8 -*-
"""University prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/136aCHRDOW_xgguIrejmOLwXnjsS8dbXC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("admission-prediction.csv")

dataset

dataset.drop(['Serial No.'],axis=1,inplace=True)

dataset.info()

dataset.corr()

import seaborn as sns
sns.boxplot(dataset["GRE Score"])

sns.boxplot(dataset["TOEFL Score"])

sns.boxplot(dataset["University Rating"])

sns.boxplot(dataset["SOP"])

sns.boxplot(dataset["CGPA"])

sns.boxplot(dataset["Research"])

plt.figure(figsize=(10,10))
sns.heatmap(dataset.iloc[:,0:9].corr(),annot=True)

dataset.isnull().any()

x = dataset.iloc[:,0:7].values
y = dataset.iloc[:,7:8].values

x.shape

y.shape

y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=4)

x_train.shape

y_train.shape

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

y_pred

y_test

import pickle
pickle.dump(regressor,open('Chance of Admit.pkl','wb'))
model = pickle.load(open('Chance of Admit.pkl','rb'))

from sklearn.metrics import r2_score
accuracy = r2_score(y_test,y_pred)

accuracy

yp = regressor.predict([[337,118,4,4.5,4.5,9.65,1]])

yp