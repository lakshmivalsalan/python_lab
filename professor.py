# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived from Person
class Employee(Person):
    def __init__(self, name, age, EmpID):
        super().__init__(name, age)
        self.EmpID = EmpID
    
    def display(self):
        super().display()
        print(f"Employee ID: {self.EmpID}")

# Derived from Employee
class Faculty(Employee):
    def __init__(self, name, age, EmpID, department):
        super().__init__(name, age, EmpID)
        self.department = department
    
    def display(self):
        super().display()
        print(f"Department: {self.department}")

# Separate class
class Researcher:
    def can_do_research(self):
        return "This person can conduct research."

# Final class
class Professor(Faculty, Researcher):
    def __init__(self, name, age, EmpID, department):
        Faculty.__init__(self, name, age, EmpID, department)
    
    def display(self):
        print("---- Professor Details ----")
        super().display()
        print(self.can_do_research())

# Creating an object of Professor
prof = Professor("Dr. Lakshmi", 40, "EMP102", "Computer Science")
prof.display()
