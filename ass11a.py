# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:17:39 2020

@author: user
"""

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
data = pd.read_csv ("D:/payal program/Python/covid19_india.csv - covid19_india.csv.csv",index_col="Sno")
print (data)
df=pd.DataFrame(data)
conf=data['Confirmed']
print(conf)
state=data[['State/UnionTerritory','Confirmed']]
print(state)
cured=data[['State/UnionTerritory','Cured']]
print(cured)
state5 = data.iloc[4]
print(state5)
df1 = df.iloc[0:4]
print(df1)
merge=pd.merge(state,cured, on='State/UnionTerritory', how='inner')
print(merge)
sb.countplot(data['Cured'])
plt.show()
with sb.axes_style('white'):
 sb.jointplot("Confirmed", "Cured", data, kind='hex')
State= data ['State/UnionTerritory'].tolist()
cured = data ['Cured'].tolist()
plt.plot(State,cured , label = 'State wise Cured')
profitList = df ['Confirmed'].tolist()
monthList = df ['Cured'].tolist()
plt.bar(monthList, profitList, label = '')
plt.show()
