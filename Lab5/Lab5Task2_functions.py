def is_secret_guessed(secret_word, aList):
    for letter in aList:
        if letter not in secret_word:
            return False
        return True 
    
str = "Love"
letter = ["L", "o", "v", "e"]
print(is_secret_guessed(str,letter))