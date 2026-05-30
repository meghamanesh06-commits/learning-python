import random

diceRolls = 100
outcome = 6
result = outcome*[0]
for rollCount in range(diceRolls):
    roll = random.randint(1, outcome)
    result[roll-1]= result[roll-1]+1
print("Dice 1:", result[0], "times\nDice 2:", result[1], "times\nDice 3:", result[2], "times\nDice 4:", result[3], "times\nDice 5:", result[4], "times\nDice 6:", result[5], "times")