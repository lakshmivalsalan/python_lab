class Currency:
    def __init__(self, amount, unit):
        self.amount = amount    
        self.unit = unit        
    
    def __eq__(self, other):
        # Two currencies are equal if both amount and unit are same
        return self.amount == other.amount and self.unit == other.unit


# Creating objects
c1 = Currency(100, "INR")
c2 = Currency(100, "INR")
c3 = Currency(100, "USD")

# Sample run
print(c1 == c2)   # True
print(c1 == c3)   # False
