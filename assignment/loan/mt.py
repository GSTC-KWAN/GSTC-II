# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:50:03 2019

@author: dell
"""

import pandas as pd
import numpy as np
import gc
import json
# Create your views here.
import joblib 
from sklearn.preprocessing import StandardScaler

BNB=joblib.load("classifier.joblib")

a=[10]
b=[10]

a=pd.DataFrame(a)
b=pd.DataFrame(b)

output= pd.DataFrame({"0":a[0],"1":b[0]})
output.to_csv('KKMtest.csv', index = False,header=False)


data_train = pd.read_csv('KKMtest.csv',lineterminator='\n',header=None)

X = data_train.iloc[:, [0,1]].values


"""      
sc_X = StandardScaler()
X = sc_X.fit_transform(X)
"""     
   
pred=BNB.predict(X)



