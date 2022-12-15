import re
import string

# Count quantity of each item in text file 
def GroceryCount():
    f = open("GroceryList.txt","r")
    items = f.readlines()
    counts = {}

    # Iterate over list
    for item in items:
        item = item.replace("\n","")

        # New item not catalogued
        if item not in counts.keys():
            counts[item] = 1

        # Add quantity
        else:
            counts[item] += 1

    for key in counts.keys():
        print(key,":", counts[key])

    f.close()
    return 0

# Count quantity of selected item
def ItemFrequency(grocery):
    grocery = grocery.capitalize()
    f = open("GroceryList.txt","r")
    items = f.readlines()
    count = 0

    for item in items:
        item = item.replace("\n","")

        if item == grocery:
            count += 1

    print(grocery,":",count)
    f.close()

    return 0

def Histogram():
    f = open("GroceryList.txt","r")
    items = f.readlines()
    counts = {}

    # Iterate over list
    for item in items:
        item = item.replace("\n","")

        # New item not catalogued
        if item not in counts.keys():
            counts[item] = 1

        # Add quantity
        else:
            counts[item] += 1

    # Iterate through keys
    for key in counts.keys():
        key = key.replace("\n","")
        num = ""
        # Count asterisks for each key
        for i in range(0,counts[key]):
            num += "*"
        print(key,num)

    f.close()

    return 0



    

