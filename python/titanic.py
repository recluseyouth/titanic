# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 17:13:14 2018

@author: User
"""
from sklearn import preprocessing 
from sklearn.model_selection import GridSearchCV 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.ensemble import RandomForestRegressor

import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os as os

import preprocess.preprocessing_titanic as pp_titanic

train = pd.read_csv("../resources/train.csv")
test = pd.read_csv("../resources/test.csv")
submit = pd.read_csv("../resources/gender_submission.csv")

dataInfo = pp_titanic.dataView(train)
print(dataInfo.head5)
print(dataInfo.info)

