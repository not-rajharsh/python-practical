''' Write a program that accepts a character and performs the following:
a. print whether the character is a letter or numeric digit or a special character.
b. if the character is a letter, print whether the letter is uppercase or lowercase
c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is NINE)
'''

digits = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]

char = input("Enter a Character:")

if char.isalpha():
    print("Character is a letter of alphabet")
    if char.islower():
        print("Letter is Lowercase")
    else:
        print("Letter is Uppercase")

elif char.isnumeric():
    print("Character is a Numeric Digit")
    if len(char) == 1:
        print(digits[int(char)])
    else:
        print("Please enter a single character")

elif not char.isalnum():
    print("This is Special Character")

