# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:22:13 2020

@author: sruth
"""

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([0, -2, 5, 10]))
