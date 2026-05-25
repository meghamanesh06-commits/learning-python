# write a program to get an integer number from a user, the number must be an even number between 10 and 50. 
# your program should generate a random number between 10 and 100 and check if the generated number is divisble by 7
# display the generated number 
# then if the first number is greater than or equivalet to the generated number, add them and display the result, otherwise get them multiplied and display the output. 

import random 
number = int(input("enter an even number between 10 and 50:"))

if number % 2 != 0 or not (10 <= number <= 50):
    print("please enter an EVEN number between 10 and 50")
else:
    generatedNumber = random.randint(10,100)
    print("Generated number is;", generatedNumber)
    if generatedNumber % 7 == 0:
        if number >= generatedNumber:
            print("the sum is:", number + generatedNumber)
        else:
            print("the product is:", number * generatedNumber)
    else:
        print("the generated number is not divisible by 7")