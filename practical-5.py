'''5. Write a program to perform the following operations on a string
a. Find the frequency of a character in a string.
b. Replace a character by another character in a string.
c. Remove the first occurrence of a character from a string.
d. Remove all occurrences of a character from a string.
'''
count = 0

string = input("Enter a string:")

#a

ch = input("Enter a character:")
for i in string:
    if i == ch:
        count+=1    
print("The Character", ch ,"appeared", count ,"times")

#b

c1 = input("Enter a character to be replaced:")
c2 = input("Enter the character to be replaced with:")
print(string.replace(c1, c2))

#c

rem = input("Enter a character to be removed:")
print(string.replace(rem, "", 1))

#d

rem_all = input("Enter a character to remove its all occurence:")
print(string.replace(rem_all, ""))