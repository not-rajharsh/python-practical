'''Write a program to accept a name from a user. Raise and handle appropriate exception(s)
if the text entered by the user contains digits and/or special characters.
'''
class InvalidNameError(Exception):
    pass


try:
    name = input("Enter your name: ")
    if not name.replace(" ", "").isalpha() or not name.strip():
        raise InvalidNameError("Name cannot contain digits or special characters.")
    print(f"Welcome, {name}!")

except InvalidNameError as error:
    print(f"Exception caught: {error}")