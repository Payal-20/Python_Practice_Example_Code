# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:56:17 2022

@author: user
"""

# -- coding: utf-8 --
"""
Spyder Editor

This is a temporary script file.
"""
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice Cream', 'Eggs']]

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

dataset

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)

df = pd.DataFrame(te_ary, columns = te.columns_)
df

from mlxtend.frequent_patterns import apriori

frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
frequent_itemsets

from mlxtend.frequent_patterns import association_rules
res = association_rules(frequent_itemsets, metric = "confidence", min_threshold=0.7)
res

res1 = res[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
res1

res2 = res1[res1['confidence']>=1]
res2