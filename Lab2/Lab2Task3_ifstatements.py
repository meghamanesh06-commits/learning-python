# Now consider a biased coin. Write a program that takes a value of p, with a range between 0 and 1 
# input from the user and then get a random number between 0 and 1 which simulates the coin flip similar to the previous program.
# If value p is greater than the random number, print head otherwise print tail.

import random 
p = float(input("Enter the probability of the flip:"))

flip = random.random()

if flip >= p:
    print("Head")
else: 
    print("Tail")
