import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib import style
style.use('fivethirtyeight')
from sklearn.tree import DecisionTreeClassifier 
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import cross_validate 
import scipy.stats as sps
# Load in the data and define the column labels
dataset = pd.read_csv('data\mushroom.csv',header=None) 
dataset = dataset.sample(frac=1) 
dataset.columns 	= 	['target','cap-shape','cap-surface','cap-color','bruises','odor','gillattachment','gill-spacing',
             'gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surfacebelow-ring','stalk-color-above-ring',
             'stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-printcolor','population',
             'habitat']
# Encode the feature values from strings to integers since the sklearn DecisionTreeClassifier only takes numerical values for label in dataset.columns:     dataset[label] = LabelEncoder().fit(dataset[label]).transform(dataset[label])
    
    
Tree_model = DecisionTreeClassifier(criterion="entropy",max_depth=1)
X	= dataset.drop('target',axis=1)
Y	= dataset['target'].where(dataset['target']==1,-1)
predictions = np.mean(cross_validate(Tree_model,X,Y,cv=100)['test_score'])
print('The accuracy is: ',predictions*100,'%')
