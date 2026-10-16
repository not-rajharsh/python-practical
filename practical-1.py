
#Write a program to find the roots of a quadratic equation

def get_roots(a, b, c):
    if a == 0:
        print("This is not a Quadratic Equation")
        return None
    else:
        disc = b**2 - 4*a*c

        if disc > 0:
            print("Equation has Two distinct real roots.")
            root1 = (-b + (disc**0.5))/(2*a)
            root2 = (-b - (disc**0.5))/(2*a)
            print(root1,root2)

        elif disc == 0:
            root = -b / (2*a)
            print("the equation has one repeated real root.")
            print(root)

        else:
            print("Equation has Two complex roots.")
            root1 = (-b + (disc**0.5))/(2*a)
            root2 = (-b - (disc**0.5))/(2*a)
            print(root1,root2)



x = int(input("Enter the coefficient of x^2:"))
y = int(input("Enter the coefficient of x:"))
z = int(input("Enter the constant:"))

get_roots(x,y,z)
