# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:15:47 2020

@author: user
"""

import pandas as pd 
df = pd.read_csv (r'D:/payal program/Python/covid19_india.csv - covid19_india.csv.csv')  
#read the csv file (put 'r' before the path string to address any special characters in the path, such  #as '\'). Don't forget to put the file name at the end of the path + ".csv" 
print (df) 