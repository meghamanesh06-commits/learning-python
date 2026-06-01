def joinList(aList, seperator):
    string = str(aList[0])
    for i in range(1, len(aList)):
        string = string + seperator + str(aList[i])
    return string 

aList = ["apple", 7, "mango", "orange"]
print(joinList(aList, "*"))