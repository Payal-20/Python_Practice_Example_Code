# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:17:20 2020

@author: user
"""

class name:
    def __init__(self,fname):
        self.fname=fname
        def __add__(self,lname):
            return self.fname+lname
        if __name__=='__main__':
         name1=name('Payal')
        print(name1+'Bhor')
            