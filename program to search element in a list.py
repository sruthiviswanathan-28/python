# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:57:55 2020

@author: sruth
"""

def search(list,n): 
    for i in range(len(list)): 
        if list[i] == n: 
            return True
    return False 
list = [1, 2, 'India', 4,'cricket', 6] 
n = 'India'
if search(list, n): 
    print("Found") 
else: 
    print("Not Found")