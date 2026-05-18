#taking an input as string representing a user's name.
#this program should output the length of the name, and the number of times each vowel occurs in it
#using the count fuction to count the number of times each vowel occurs in the name 

name = input("Enter your name:")

length = len(name)

num_a = name.count("a")
num_e = name.count("e")
num_i = name.count("i")
num_o = name.count("o")
num_u = name.count("u")

print("The length of your name is:", length)
print("The number of times a occurs in", name, "is:", num_a)
print("The number of times e occurs in", name, "is:", num_e)
print("The number of times i occurs in", name, "is:", num_i)
print("The number of times o occurs in", name, "is:", num_o)
print("The number of times u occurs in", name, "is:", num_u)