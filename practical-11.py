'''Write a function that prints a dictionary where the keys are numbers between 1 and 5
and the values are cubes of the keys.'''

def cube():
    cub = {}
    for i in range(1,6):
        c = i*i*i
        cub.update({i:c})
    print(cub)
cube()