# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 14:58:16 2020

@author: user
"""

import seaborn as sns
import pandas as pd 
import numpy as np
sns.set() 
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000) 
data = pd.DataFrame(data, columns=['x', 'y']) 
for col in 'xy':     sns.kdeplot(data[col], shade=True)
for col in 'xy':     sns.kdeplot(data[col], shade=True) 
