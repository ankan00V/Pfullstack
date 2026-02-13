#simple inheritance

#create a class person with attributes name and method display()
#create a class student that inherits from person, adds attribute roll_no and display() method
"""class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):
        super().display()
        print(f"Roll No: {self.roll_no}")

p=Person("ashok")
p.display() 
s=Student("rashmi", 101)
s.display()"""

#create a class animal with attributes category and method sound()
#create a class dog that inherits from animal and overrides sound() method
class Animal:
    def __init__(self, category):
        self.category = category

    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, category, breed):
        super().__init__(category)
        self.breed = breed

    def sound(self):
        print("Bark")

a=Animal("Mammal")
a.sound()
d=Dog("Mammal", "Labrador")
d.sound()