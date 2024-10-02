class Parrot:
    # Class Variable
    species = "Bird"

    # Constructor
    def __init__(self, name, age):
       # instance Variable
       self.name = name
       self.age = age

    # Method
    def display(self):
        print(f"{self.name}  is a {self.species} and it's age is {self.age}")

# Create the object
Pihu = Parrot("Pihu", 3)
Pihu.display()

Woo = Parrot("Woo", 4)
Woo.display()