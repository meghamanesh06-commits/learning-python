#making an annoying number guessing game 

import random 

target = random.randint(1,100)

trial = int(input("please enter a number between 1 and 100:"))

if trial > target:
    print ("too big")
elif trial < target:
    print ("too small")
else: 
    print ("you win!")
