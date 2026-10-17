'''
Write a program to create a list of the cubes of only the even integers appearing in the
input list (may have elements of other types also) using the following:
a. 'for' loop
b. list comprehension'''

def cube_even_for(input_list):
    result = []
    for item in input_list:
        if isinstance(item, int) and not isinstance(item, bool):
            if item % 2 == 0:
                result.append(item ** 3)
    return result

data = [1, 2, 3, 4, "hello", 6.5, True, 6]
print(cube_even_for(data)) 




def cube_even_comprehension(input_list):
    return [
        item ** 3 
        for item in input_list 
        if isinstance(item, int) and not isinstance(item, bool) and item % 2 == 0
    ]
data = [1, 2, 3, 4, "hello", 6.5, True, 6]
print(cube_even_comprehension(data)) 