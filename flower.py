class Flower:
    def __init__(self, name):
        self.name = name

    def display(self):
        if hasattr(self, "petalColor"):
            print(f"{self.petalColor} {self.name}")
        else:
            print("Unknown Flower")


# Creating flower objects
f1 = Flower("Rose")
f1.petalColor = "Red"       # Adding attribute at runtime

f2 = Flower("Lotus")        # No color added

# Displaying results
f1.display()   # Output: Red Rose
f2.display()   # Output: Unknown Flower