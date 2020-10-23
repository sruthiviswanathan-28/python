# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 22:44:10 2020

@author: sruth
"""

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list
duplicate=[1,2,3,4,3,2,6,4,7]
print(Remove(duplicate))