# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:17:35 2020

@author: user
"""

class String: 
      
    # magic method to initiate object 
    def __init__(self, string): 
        self.string = string 
          
    # print our string object 
    def __repr__(self): 
        return 'Payal {}'.format(self.string) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # object creation 
    string1 = String('Bhor') 
  
    # print object location 
    print(string1) 