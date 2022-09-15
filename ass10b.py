# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:52:06 2020

@author: user
"""

import seaborn as sb
import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("D:/payal program/Python/indian_food.csv - indian_food.csv")
sb.countplot(data['prep_time'])
plt.show()
sb.countplot(data['cook_time'])
data.head()
with sb.axes_style('white'):
    sb.jointplot("prep_time", "cook_time", data, kind='hex')
with sb.axes_style('white'):
    sb.jointplot("prep_time", "cook_timeh", data, kind='kde')
