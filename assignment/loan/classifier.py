# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:51:01 2019

@author: dell
"""

import pandas as pd
import numpy as np
from joblib import dump
from sklearn.naive_bayes import BernoulliNB



data_train = pd.read_csv('Trainset.csv',lineterminator='\n',header=None)

X = data_train.iloc[:, [0,1]].values

y = data_train.iloc[:, 2].values




from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=1000,random_state=0)
classifier.fit(X,y)


'''
model = BernoulliNB()
model.fit(X, y)
'''

dump(classifier, 'classifier.joblib')



