# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:42:20 2020

@author: user
"""

class string:
    def __init__(self, string):
        self.string=string
        def __add__(self,other):
            return self.string + ' '+ other
        if __name__=='__main__':
            name=str(input("enter your first name:"))
            srname=str(input("enter your last name:"))
            string1 = string(name)
            print(string1._add__(srname))