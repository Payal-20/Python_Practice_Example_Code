# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 16:47:09 2022

@author: user
"""
#1
from copy import deepcopy
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib import pyplot as plt
#2
center_1 = np.array([2,1])
center_2 = np.array([5,5])
center_3 = np.array([8,7])

# Generate random data and center it to the three centers
data_1 = np.random.randn(200, 2) + center_1
data_2 = np.random.randn(200,2) + center_2
data_3 = np.random.randn(200,2) + center_3

data = np.concatenate((data_1, data_2, data_3), axis = 0)

plt.scatter(data[:,0], data[:,1], s=7)
#3
k = 2
# Number of training data
n = data.shape[0]
# Number of features in the data
c = data.shape[1]

# Generate random centers, here we use sigma and mean to ensure it represent the whole data
mean = np.mean(data, axis = 0)
std = np.std(data, axis = 0)
centers = np.random.randn(k,c)*std + mean

# Plot the data and the centers generated as random
plt.scatter(data[:,0], data[:,1], s=7)
plt.scatter(centers[:,0], centers[:,1], marker='*', c='g', s=150)
#4
centers_old = np.zeros(centers.shape) # to store old centers
centers_new = deepcopy(centers) # Store new centers

data.shape
clusters = np.zeros(n)
distances = np.zeros((n,k))

error = np.linalg.norm(centers_new - centers_old)

# When, after an update, the estimate of that center stays the same, exit loop
while error != 0:
    # Measure the distance to every center
    for i in range(k):
        distances[:,i] = np.linalg.norm(data - centers[i], axis=1)
    # Assign all training data to closest center
    clusters = np.argmin(distances, axis = 1)
    
    centers_old = deepcopy(centers_new)
    # Calculate mean for every cluster and update the center
    for i in range(k):
        centers_new[i] = np.mean(data[clusters == i], axis=0)
    error = np.linalg.norm(centers_new - centers_old)
centers_new    
#5
plt.scatter(data[:,0], data[:,1], s=7)
plt.scatter(centers_new[:,0], centers_new[:,1], marker='*', c='g', s=150)
#6
df = pd.read_csv("Data1.csv") #load the dataset
df.drop('Year',axis=1,inplace=True) # Se elimina la columna no requerida
#7
df.head()
#8
df["Tmin"] = pd.Categorical(df["Tmin"])
df["Tmin"] = df["Tmin"].cat.codes
# Change dataframe to numpy matrix
data = df.values[:, 0:4]
category = df.values[:, 4]
#9
k = 2
# Number of training data
n = data.shape[0]
# Number of features in the data
c = data.shape[1]

# Generate random centers, here we use sigma and mean to ensure it represent the whole data
mean = np.mean(data, axis = 0)
std = np.std(data, axis = 0)
centers = np.random.randn(k,c)*std + mean

# Plot the data and the centers generated as random
colors=['orange', 'blue', 'green']
for i in range(n):
    plt.scatter(data[i, 0], data[i,3], s=3, color = colors[int(category[i])])
plt.scatter(centers[:,0], centers[:,1], marker='*', c='g', s=150)
#10
centers_old = np.zeros(centers.shape) # to store old centers 
centers_new = deepcopy(centers) # Store new centers 
data.shape 
clusters = np.zeros(n) 
distances = np.zeros((n,k)) 
error = np.linalg.norm(centers_new - centers_old) # When, after an update, the estimate of that center stays the same, exit loop while error != 0: # Measure the distance to every center 
for i in range(k): 
  distances[:,i] = np.linalg.norm(data - centers[i], axis=1) # Assign all training data to closest center 
  clusters = np.argmin(distances, axis = 1) 
  centers_old = deepcopy(centers_new) # Calculate mean for every cluster and update the center 
  for i in range(k): centers_new[i] = np.mean(data[clusters == i], axis=0) 
  error = np.linalg.norm(centers_new - centers_old) 
  centers_new




