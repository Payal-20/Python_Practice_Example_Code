# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:16:32 2020

@author: user
"""

scr=(input("Enter the Score: "))

try:

   scr=float(scr)

   if scr>=0.0 and scr<=1.0:

       if scr >= 0.9:

           print("A")

       elif scr >= 0.8:

           print("B")

       elif scr >= 0.7:

           print("C")

       elif scr >= 0.6:

           print("D")

       elif scr<0.6:

           print("F")

   else:

       print("Out Of range")

except:

   print("Try a number")