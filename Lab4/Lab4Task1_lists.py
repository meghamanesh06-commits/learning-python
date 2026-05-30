numList = []
sqrList = []
count = 0

while count < 5:
    temp = int(input("enter a number:"))
    numList.append(temp)
    sqrList.append(temp*temp)
    count += 1

print("The entered numbers are:", numList)
print("The numbers squared are:", sqrList)