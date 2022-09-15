myDict = {
    "pankha": "fan",
    "Dabba": "box",
    "vastu": "item"
}
print("options are", myDict.keys())
a=input("enter the hindi word\n")
print("meaning of your word is:\n",myDict.get(a))