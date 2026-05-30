#write a program to calculate the following 
# Sum = 2/2! - 4/4! + 6/6! - 8/8!

fact = 1 
sign = 1
result = 0 
count = 1

while count <= 8:
    fact = fact * count 
    result = result + (sign * count/fact)
    sign = -sign 
    count = count +1

print("The output of the series is:", round(float(result),2))