# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:38:17 2020

@author: user
"""

import pandas as pd 
df = pd.read_csv (r'D:/payal program/Python/indian_food.csv - indian_food.csv.csv')  
#read the csv file (put 'r' before the path string to address any special characters in the path, such  #as '\'). Don't forget to put the file name at the end of the path + ".csv" 
print (df) 
df=pd.read_csv("indian_food.csv - indian_food.csv.csv",index_col="name") 
print(df) 
df[:'Balu shahi']
df=pd.read_csv("indian_food.csv - indian_food.csv",index_col="name") 
print(df)
df[:'Balu shahi'] 
df['Boondi':'Til Pitha'] 
concat = [df[:'Balu shahi'],df['Boondi':'Til Pitha']] 
concat 
df = pd.read_csv ('indian_food.csv - indian_food.csv')  
print(df)
grouped = df.groupby('state') 
grouped.first() 

