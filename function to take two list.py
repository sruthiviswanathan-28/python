# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 22:52:55 2020

@author: sruth
"""

def common_data(list1, list2):
   result = False
   for x in list1:
    for y in list2:
          if x == y:
            result = True
            return result
print(common_data([1,2,3,4,5],[5,6,7,8,9]))
print(common_data([1,2,3,4,5],[6,7,8,9]))