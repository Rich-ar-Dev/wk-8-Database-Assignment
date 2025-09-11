# Activity 2: Polymorphism Challenge 🎭

class Animal:
    def move(self):
        print("The animal moves...")

class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")

class Bird(Animal):
    def move(self):
        print("The bird flies 🐦")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")


# Example usage with polymorphism
animals = [Dog(), Bird(), Fish()]

for a in animals:
    a.move()   # Each class defines move() differently
