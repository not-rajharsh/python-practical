class InvalidNameError(Exception):
    pass

def validate_name(name):
    if not name.strip():
        raise InvalidNameError("Name cannot be empty.")
    if not all(c.isalpha() or c.isspace() for c in name):
        raise InvalidNameError("Name must contain only letters and spaces.")
    return name.title()

try:
    name = input("Enter your name: ")
    print("Hello,", validate_name(name))
except InvalidNameError as e:
    print("Invalid name:", e)
finally:
    print("Program finished.")
