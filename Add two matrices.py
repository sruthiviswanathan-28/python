# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 23:50:40 2020

@author: sruth
"""

X = [[1,2,3],    [4,5,6],    [7 ,8,9]]
Y = [[5,6,7],    [7,8,9],    [2,3,4]]

result = [[0,0,0],  [0,0,0],  [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
       print(result)