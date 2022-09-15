# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:03:25 2020

@author: user
"""
import pandas as pd
SYIT={'Studentname':['51','52','53','54'],
      'GTC':[12,22,15,32],
      'CAMBS':[17,14,3,5],
      'PPL1':[15,48,31,5]
      }
df=pd.DataFrame(SYIT,columns=['Studentname','GTC','CAMBS','PPL1'])
print(df)
df.loc[df['GTC']<8]
df.loc[df['CAMBS']<8]
df.loc[df['PPL1']<8]

df.loc[df['GTC']>15]
df.loc[df['CAMBS']>15]
df.loc[df['PPL1']>15]


