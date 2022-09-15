sub1=int(input("enter first sub marks:"))
sub2=int(input("enter second sub marks:"))
sub3=int(input("enter third sub marks:"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are failed due to one of the sub. is less than 33")
elif(sub1+sub2+sub3)/3 <40:
    print("you are failed because percentage is less than 40")
else:
    print("you are passed")