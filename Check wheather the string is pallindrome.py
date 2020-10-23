# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 00:13:27 2020

@author: sruth
"""

my_string=input("Enter string:")
if(my_string==my_string[::-1]):
   print("The string is a palindrome")
else:
   print("The string isn't a palindrome")