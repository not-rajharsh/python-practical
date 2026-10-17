'''Write a program to define a class Point with coordinates x and y as attributes. Create
relevant methods and print the objects. Also define a method distance to calculate the
distance between any two point objects.'''

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance(self, other):
        return (((other.x - self.x) ** 2 + (other.y - self.y) ** 2)**0.5)
    
p1 = Point(1, 2)
p2 = Point(4, 6)

print("First Point:", p1)
print("Second Point:", p2)

dist = p1.distance(p2)
print(f"The distance between {p1} and {p2} is: {dist:.2f}")