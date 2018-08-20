# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 09:21:37 2018

@author: sharda
"""
number = int(input("Enter a number to find the square root : "))
if number < 0 :
  print("Please enter a valid number.")
else :
  sq_root = number ** 0.5
  print("Square root of {} is {} ".format(number,sq_root))