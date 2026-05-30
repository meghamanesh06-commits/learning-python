n = int(input("enter a number:"))
maxDigit = len(str(abs(n)))
count = 0 
for count in range(n+1):
    diff = maxDigit - len(str(abs(count)))
    if diff>0:
        count = "0" * diff + str(count)
    print(count)