#6. Write a program to swap the first n characters of two strings.

str1 = input("Enter the first string:")
str2 = input("Enter the second string:")

n = int(input("Enter the value of n:"))

if len(str1) < n or len(str2) < n:
    print("Please enter a valid value (strings must be at least n characters long).")
else:
    prefix1 = str1[:n]
    prefix2 = str2[:n]
    new_str1 = prefix2 + str1[n:]
    new_str2 = prefix1 + str2[n:]
    print('First swapped string is:', new_str1)
    print('Second swapped string is:', new_str2)
    