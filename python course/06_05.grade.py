marks=int(input("enter your marks: "))
if(marks>90):
    garde="Ex"
elif(marks>80):
    garde="A"
elif(marks>70):
    garde="B"
elif(marks>60):
    garde="C"
elif(marks>50):
    garde="D"
else:
    grade="F"
print("your grade is "+ grade)