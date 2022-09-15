# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:26:39 2020

@author: user
"""

def computepay(h,r):

    if h > 40:

        p = 1.5 * r * (h - 40) + (40 *r)

    else:

        p = h * r

    return p

    

hrs = input("Enter Hours:")

hr = float(hrs)

rphrs = input("Enter rate per hour:")

rphr = float(rphrs)

p = computepay(hr,rphr)

print(p)
