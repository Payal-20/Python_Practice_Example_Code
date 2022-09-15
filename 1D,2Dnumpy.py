# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:58:11 2020

@author: payal
"""

import numpy as np
arr1=np.arange(1,7)
arr1=arr1.reshape(2,3)
arr2=np.array([[10,25,5],[19,37,20]])
print("array 1 is",arr1)
print("array 2 is ",arr2)
print("addition of array is")
print(np.add(arr1,arr2))
print("Substraction of array is")
print(np.subtract(arr2,arr1))
print("Division of array is")
print(np.divide(arr2,arr1))
print("Multiplication of array is")
print(np.multiply(arr1,arr2))