def smallestAbsoluteValue(list_given):
    smallest = list_given[0]
    for anItem in list_given:
        if absVal(anItem) < absVal(smallest):
            smallest = anItem
    return smallest

def absVal(num):
    if num < 0:
        return -num
    return num

numList = [3, -5, 2, -6, -1]
print(smallestAbsoluteValue(numList))