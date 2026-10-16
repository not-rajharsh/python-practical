#Write a program to create a pyramid of the character ‘*’ and a reverse pyramid
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)

print()

for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '* ' * i)