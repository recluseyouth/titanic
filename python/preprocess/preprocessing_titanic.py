# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 18:27:11 2018

@author: User
"""

class DataInf ():
    def __init__(self, head5, info):
        self.head5 = head5
        self.info = info
   
def dataView(train):
    dataInfo = DataInf(train.head(5), train.head(10))
    print(dataInfo.head5)
    print(dataInfo.info)
    return dataInfo