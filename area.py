# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:22:50 2020

@author: user
"""

class Triangle:     
 print("******Area Calculator******") 
 def area1(self):        
    print("\nArea Of Triangle:-") 
    self.h=int(input("Enter height : ")) 
    self.b=int(input("Enter base : ")) 
    return 0.5*self.h*self.b 
 
class Rectangle: 
 def area2(self):         
     print("\nArea Of Rectangle:-") 
     self.l=int(input("Enter the length : ")) 
     self.b=int(input("Enter the breadth : ")) 
     return self.l*self.b 
 
 
class Square(Triangle,Rectangle): 
    def area3(self):         
        print("\nArea Of Square:-") 
        self.x=int(input("Enter the side of square : ")) 
        return self.x*self.x 
 
 
s=Square() 
 
choice=0 
while choice!=4:     
    print("1. Triangle")    
    print("2. Rectangle")    
    print("3. Square")     
    print("4. Exit")     
    choice=int(input("Enter your choice: "))     
    if choice==1: 
        print(" --> Area of Triangle is: ",s.area1()) 
    elif choice==2: 
        print(" --> Area of Rectangle is: ",s.area2())
    elif choice==3:
        print(" --> Area of Square is: ",s.area3()) 
    elif choice==4: 
        print("*****Thank you!*****")     
    else: 
        print("Invalid choice!! Please try again!!") 
 
 
