import math

class Complex:
    def __init__(self, real=0, imag=0):
        self.__real = real
        self.__imag = imag

    
    def magnitude(self):
        return math.sqrt(self.__real ** 2 + self.__imag ** 2)

   
    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    
    def __str__(self):
        return f"{self.__real} + {self.__imag}i"


c1 = Complex(3, 4)  
c2 = Complex(1, 7)   

print(f"Comparing: {c1} >= {c2} ?")

if c1 >= c2:
    print("c1 is greater or equal.")
else:
    print("c2 is greater.")
