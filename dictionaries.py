colors = {1 : "Blue" ,
          2 : "Red" ,
          3 : "Green" ,
          4 : "Yellow" ,
          5 : "Purple" }

newDict = dict()

for key, value in colors.items():

    if len(value)<7:
        newDict[key] = value

print(newDict)
    