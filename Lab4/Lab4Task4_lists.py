word = input("enter a word:")

check = True 
wordLen = len(word)
upperLim = wordLen // 2

for charCount in range(upperLim):
    if word[charCount] != word[wordLen - charCount - 1]:
        check = False
        break
if check: 
        print("palindrome")
else:
        print("not a palindrome")