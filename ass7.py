# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:41:34 2020

@author: user
"""

import pandas as pd 
record ={'Name':['Sakshi','Vaibhav','Sayali','Ankita','Payal','Akanksha','Anjali','Nikita','Pooja','Prasad'],
         'Marks_GTC':[8,16,18,12,5,15,11,7,13,11],
         'Marks_CAMBS':[11,19,14,1,3,17,18,0,7,12],
         'Marks_PPL1':[17,1,13,9,5,11,21,19,1,14] 
        } 
dataframe = pd.DataFrame(record, columns = ['Name', 'Marks_GTC', 'Marks_CAMBS', 'Marks_PPL1']) 
print("Given Dataframe :\n", dataframe) 

rslt_df = dataframe.drop(['Marks_CAMBS','Marks_PPL1'],axis=1)
rslt_df1 = rslt_df[dataframe['Marks_GTC'] < 8]
print('\nStudents Who failed in GTC\n', rslt_df1)

rslt_df2 = dataframe.drop(['Marks_GTC','Marks_PPL1'],axis=1)
rslt_df3 = rslt_df2[dataframe['Marks_CAMBS'] < 8]
print('\nStudents Who failed in CAMBS\n', rslt_df3)

rslt_df4 = dataframe.drop(['Marks_GTC','Marks_CAMBS'],axis=1)
rslt_df5 = rslt_df4[dataframe['Marks_PPL1'] < 8]
print('\nStudents Who failed in PPL1\n', rslt_df5)

rslt_df6 = dataframe.drop(['Marks_PPL1','Marks_CAMBS'],axis=1)
rslt_df7 = rslt_df6[dataframe['Marks_GTC'] >15]
print('\nStudents Who got more than 15 marks in GTC\n', rslt_df7)

rslt_df8 = dataframe.drop(['Marks_GTC','Marks_PPL1'],axis=1)
rslt_df9 = rslt_df8[dataframe['Marks_CAMBS'] >15]
print('\nStudents Who got more than 15 marks in CAMBS\n', rslt_df9)

rslt_df10 = dataframe.drop(['Marks_GTC','Marks_CAMBS'],axis=1)
rslt_df11 = rslt_df10[dataframe['Marks_PPL1'] >15]
print('\nStudents Who got more than 15 marks in PPL1\n', rslt_df11)

