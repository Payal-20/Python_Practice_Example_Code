# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import seaborn as sb
import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("D:/payal program/Python/covid19_india.csv - covid19_india.csv.csv")
sb.distplot(data['Deaths'])
plt.show()
sb.distplot(data['Cured'])
data.head()
with sb.axes_style('white'):
    sb.distplot("Deaths", "Cured", data, kind='hex')
with sb.axes_style('white'):
    sb.distplot("Deaths", "Cured", data, kind='kde')

