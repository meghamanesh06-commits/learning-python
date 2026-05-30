#extend the program so that the start and stop values are random between 1 and 10 

import random 
start = random.randint(1,10)
end = random.randint(1,10)

result = 0
for i in range(start, end +1):
    result = result + (3 * i)

print("the result is:", result)