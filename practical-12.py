'''Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). Write a program to perform following
operations:
a. Print half the values of the tuple in one line and the other half in the next line.
b. Print another tuple whose values are even numbers in the given tuple.
c. Concatenate a tuple t2=(11,13,15) with t1.
d. Return maximum and minimum value from this tuple
'''
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

#a
mid = len(t1) // 2
print(*t1[:mid])
print(*t1[mid:])


#b
even=()
for i in t1:
    if i%2 == 0:
        even += (i,)
print("Even number from the tuple: ",even)


#c
t2=(11,13,15)
new_tuple = t1 + t2
print("New tuple: ",new_tuple)


#d
print("Max value from the new tuple :", max(new_tuple))
print("Min value from the new tuple :", min(new_tuple))