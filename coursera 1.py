# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:05:54 2020

@author: user
"""

hrs = input("enter hr:")
h=float(hrs)
rate=input("enter the rate:")
r=float(rate)
if h > 40:
    reg=40 + r
    otp=(h -40) + (r * 1.50)
    xp=reg + otp
else:
    xp=h + r
    print(xp)