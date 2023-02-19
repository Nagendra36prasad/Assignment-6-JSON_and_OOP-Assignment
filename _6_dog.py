# using oops method 

# 1. Create a class named ‘Dog’. 
# It should have a constructor which accepts its name, age and coat color.

#  You must perform the following operations:

#  a. It should have a function ‘description()’ which prints the name and age of the dog.
#  b. It should have a function ‘get_info()’ which prints the coat color of the dog.
#  c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
#  d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    def description(self):
        print(f"This is {self.name}, and it is {self.age} year old dog.")
        
    def get_info(self):
        print("{} has a {} coat color.".format(self.name, self.coat_color))
        

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def bark(self):
        print("{} is barking!".format(self.name))
        
    def hunt(self):
        print("{} is hunting!".format(self.name))
        
        
class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def snore(self):
        print("{} is snoring!".format(self.name))
        
    def guard(self):
        print("{} is guarding!".format(self.name))



dogs = Dog("Havanese", 7, "white")           # Create Dog object
dogs.description()
dogs.get_info()


my_jrt = JackRussellTerrier("JackRus", 8, "white and brown")    # Create JackRussellTerrier object
my_jrt.description()                  
my_jrt.bark()
my_jrt.hunt()


my_bulldog = Bulldog("Phoebe", 5, "white")            # Create Bulldog object
my_bulldog.description()
my_bulldog.get_info()
my_bulldog.snore()
my_bulldog.guard()
