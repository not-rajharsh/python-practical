def find_indices(first, second):
    if not second:
        return [-1]
    
    indices = []
    start = 0

    while True:
        index = first.find(second, start)
        if index == -1:
            break

        indices.append(index)
        start = index + 1

    if not indices:
        return [-1]

    return indices

print(find_indices("Yo wassup guys this is Harsh and this is python", "is"))