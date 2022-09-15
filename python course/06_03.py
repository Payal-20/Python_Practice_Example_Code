text=input("Enter the text: ")
if("i love you" in text):
    spam=True
elif("i will die without you" in text):
    spam=True
elif("i want to marry you" in text):
    spam=True
elif("you are important" in text):
    spam=True
else:
    spam=False
if(spam):
    print("This text is spam")
else:
    print("This text is not spam")