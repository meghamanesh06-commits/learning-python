# Writing a code that simulates an unbiased coin flip.
# Should print true if coin flip results in head and false if it results in tail 

import random 

coin_flip = random.random()

if coin_flip > 0.5:
    print ("Heads therefore true")
else: 
    print ("Tails therefore false ")