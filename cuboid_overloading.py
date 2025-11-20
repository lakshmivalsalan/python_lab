class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height

    
    def __le__(self, other):
        if isinstance(other, Cuboid):
            return self.volume() <= other.volume()
        return NotImplemented

    def display(self):
        print(f"Length: {self.length}, Breadth: {self.breadth}, Height: {self.height}")
        print(f"Volume: {self.volume()}")



cuboid1 = Cuboid(2, 3, 4)
cuboid2 = Cuboid(3, 3, 3)

cuboid1.display()
print()
cuboid2.display()
print()


if cuboid1 <= cuboid2:
    print("Cuboid1 has volume less than or equal to Cuboid2")
else:
    print("Cuboid1 has volume greater than Cuboid2")
