# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:32:06 2020

@author: user
"""

# Definig a class vehicle, which contain 
# name and colour and modelno and price of the vehicle

class vehicle(object):
    def __init__(self, name, colour, modelno, price):
        self.name = name
        self.colour = colour
        self.modelno = modelno
        self.price = price
    def getprice(self):
        return self.price
    def getmodelno(self):
        return self.modelno
    def getcolour(self):
       return self.colour
    def __str__(self):
        return self.name + ' : ' + str(self.getprice()) +' :: '+  str(self.getmodelno()) +' :: '+  str(self.getcolour())
  
# Defining a function for building a Record 
# which generates list of all the vehicle   
def prices(rec, name, modelno, price,colour):
    rec.append(vehicle(name, price, modelno,colour))
    return rec

# Main Code
Record = []
x = 'y'
while x == 'y':
    name = input('Enter the name of the vehicle: ')
    price = input('Enter the price of model: ')
    model = input('model number: ')
    colour=input('colour of vehicle:')
    Record = prices(Record, name, price, colour,model)
    x = input('another student? y/n: ')
    
# Printing the list of vehicle
n = 1
for el in Record:
    print(n,'. ', el)
    n = n + 1
