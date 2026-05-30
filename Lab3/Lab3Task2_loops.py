start = int(input("enter the start value:"))
end = int(input("enter the end value:"))

result = 0 
c = start 
while c <= end:
    result = result + (2*(c**2) + 4*c)
    c=c+1

print("the result is:", result)