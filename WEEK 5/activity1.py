# Activity 1: Simple Animal Class with Inheritance and Polymorphism

# Parent Class: Animal
class Animal:
    def __init__(self, name):
        # Initializing the name of the animal
        self.name = name

    def speak(self):
        # Method to be overridden in subclasses
        pass

# Subclass: Dog (Inheritance and Polymorphism)
class Dog(Animal):
    def speak(self):
        # Dog-specific implementation of speak()
        print(f"{self.name} says Woof!")

# Subclass: Cat (Inheritance and Polymorphism)
class Cat(Animal):
    def speak(self):
        # Cat-specific implementation of speak()
        print(f"{self.name} says Meow!")

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method (demonstrating polymorphism)
dog.speak()  # Output: Buddy says Woof!
cat.speak()  # Output: Whiskers says Meow!
