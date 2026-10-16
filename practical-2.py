'''Write a program to accept a number ‘n’ and
a. Check if ’n’ is prime
b. Generate all prime numbers till ‘n’
c. Generate first ‘n’ prime numbers This program may be done using functions'''

prime = True

n = int(input("Enter a number:"))

if n <= 1:
    prime = False
elif n == 2:
    prime = True
elif n%2 == 0:
    prime = False

root = int(n**0.5)

for i in range(3, root+1, 2):
    if n%i == 0:
        prime = True

if prime:
    print("The Number is Prime.")
else:
    print("The Number is NOT Prime.")

