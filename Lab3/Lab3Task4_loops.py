#write a program to get 10 words from user, count those that start with a vowel letter. Assume all the words start with a capital letter. 

count = 0 
for i in range(10):
    name = input("enter a word:")
    if name[:1] == 'A' or name[:1] == 'E' or name[:1] == 'I' or name[:1] == 'O' or name[:1] == 'U':
        count = count +1
print(count)