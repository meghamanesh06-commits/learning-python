#prepare a python program that can compute the solution for the following problem using loops allowing the user to choose the start and end values.

start = int(input("enter the start value:"))
end = int(input("enter the end value:"))

result = 0  #creates a variable to keep a running total, starting at 0

for i in range(start, end +1):
    result = result + (3 * i)
print("the result is:", result) 

