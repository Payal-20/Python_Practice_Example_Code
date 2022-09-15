# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:04:05 2020

@author: user
"""

class Cricket():
 def Player(self):
  print("There are 11 players in each team.")
 def Area(self):
  print("137.16m area of ground reduired for cricket.")

 def Equipment(self):
  print("Cricket bat,batting leg-guard,golves,ball are the equipment required.")

class Football():
  def Player(self):
   print("Each team has 11 players and among these 1 is goalkeeper.")
  def Area(self):
   print("40*30 yards of ground required for football.")
  def Equipment(self):
   print("Helmet,gloves,shoes,pads,mouthguard are some equipment required.")

def func(obj):
 obj.Player()
 obj.Area()
 obj.Equipment()
obj_crk = Cricket()
obj_fot = Football()
func(obj_crk)
func(obj_fot)