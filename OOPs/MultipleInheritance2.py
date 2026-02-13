# class Vehicle:
#     def show(self):
#         print("This is Vehicle")
# class Car(Vehicle):
#     def info(self):
#         print("This is Car")
# class EV(Car):
#     def display(self):
#         print("This is an EV Car")
# ev = EV()
# ev.show()
# ev.info()
# ev.display()

# Q2
# class Person:
#     def __init__(self,name,regno):
#         self.name = name
#         self.__regno = regno
#     def show(self):
#         print("Name :-",self.name)
#         print("Regno :-",self.__regno)
# class Employee(Person):
#     def __init__(self,name,regno,sal,empid):
#         super().__init__(name,regno)
#         self.sal = sal
#         self._empid = empid
#     def info(self):
#         print("Salary :-",self.sal)
#         print("Emp ID :-",self._empid)
# class Manager(Employee):
#     def __init__(self, name, regno, sal, empid, dept):
#         super().__init__(name, regno, sal, dept)
#         self.dept = dept
#     def display(self):
#         print("Department :-",self.dept)
# m = Manager("Abir", "21CSE001", 1000000, "EMP101", "CSE")
# m.display()
# m.info()
# m.show()
# print("---------")
# print(m.name)
# print(m._empid)

# Q3
# class Animal:
#     def eat(self):
#         print("Animal Eating")
#     def _eating(self):
#         print("Eatin Protectedly")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is Barking")
#     def __barking(self):
#         print("Dog is Barking Privately")
# class Puppy(Dog):
#     def play(self):
#         print("Puppy is Playing")
#     def playing(self):
#         print("Puppy is Publicaly")
# p = Puppy()
# p.play()
# p.playing()
# p.bark()
# # p.barking()
# p.eat()
# p._eating()

# 4. Create a class Device that turns on, inherit it into Mobile that can make calls, then inherit it into Smartphone that can run apps.
# class Device:
#     def turon(self):
#         print("Turning on Device")
# class Mobile(Device):
#     def calls(self):
#         print("Mobile can make call")
# class Smartphone(Mobile):
#     def apps(self):
#         print("It can run apps")
# s = Smartphone()
# s.apps()
# s.calls()
# s.turon()

# 5. Create a class Account with balance, inherit it into SavingsAccount that adds interest, then inherit it into PremiumAccount that adds bonus features.
# class Account:
#     def __init__(self,balance):
#         self.balance = balance
#     def showbal(self):
#         print("Balance :-",self.balance)
# class SavingsAccount(Account):
#     def __init__(self, balance,interest):
#         super().__init__(balance)
#         self.interest = interest
#     def addInterest(self):
#         self.balance += self.balance*self.interest
#         print("Balance after Interest :-",self.balance)
# class PremiumAccount(SavingsAccount):
#     def __init__(self, balance, interest, bonus):
#         super().__init__(balance, interest)
#         self.bonus = bonus
#     def addBonus(self):
#         self.balance += self.bonus
#         print("Balance after Bonus :-",self.balance)
# pa = PremiumAccount(100,10,20)
# pa.showbal()
# pa.addInterest()
# pa.addBonus()

# 6. Create a class Shape, inherit it into Rectangle to calculate area, then inherit it into ColoredRectangle that adds color information.
# class Shape:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#     def show(self):
#         print("Length :-",self.length)
#         print("Breadth :-",self.breadth)
# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         super().__init__(length, breadth)
#     def area(self):
#         self.area = 2*(self.length+self.breadth)
#         print("Area :-",self.area)
# class ColoredRectangle(Rectangle):
#     def __init__(self, length, breadth,):
#         super().__init__(length, breadth)
#     def colour(self):
#         self.colour = "Yellow"
#         print("Colour :-",self.colour)
# pa = ColoredRectangle(100,10)
# pa.show()
# pa.area()
# pa.colour()
