#write a program to get a students mark, as an input from user and print its grade based on the following criteria:
# if mark >= 80 print A 
# if mark between 70 and 80 print B
# if mark between 60 and 70 print C
# if mark between 50 and 60 print D
# if mark < 50 print F

mark = int(input("Enter your mark:"))

if mark >= 80:
    print("A")
elif mark >= 70:
    print("B")
elif mark >= 60:
    print("C")
elif mark >= 50:
    print("D")
else:
    print("F")