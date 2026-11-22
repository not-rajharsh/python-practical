import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Point3D(Point2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 +
                         (self.y - other.y)**2 +
                         (self.z - other.z)**2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


a = Point3D(1, 2, 2)
b = Point3D(4, 6, 14)
print("a =", a)
print("b =", b)
print("Distance of a from origin:", a.distance_from_origin())
print("Distance between a and b:", a.distance_to(b))
