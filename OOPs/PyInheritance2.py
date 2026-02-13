# class Person:
#     def __init__(self,name):
#         self.name = name
#     def display(self):
#         print("Name :-",self.name)

# class Student(Person):
#     def __init__(self,name,rollno):
#         super().__init__(name)
#         self.rollno = rollno
#     def show(self):
#         self.display()
#         print("Roll No :-",self.rollno)

# p = Person("Anthony")
# p.display()
# s = Student("Akhil",22)
# s.show()

# class Vehicle:
#     def __init__(self,speed):
#         self.speed = speed
    
# class Bike(Vehicle):
#     def __init__(self,speed,brand):
#         super().__init__(speed)
#         self.brand = brand
# b = Bike(20,"Hero")
# print(b.speed)
# print(b.brand)

class School:
    def __init__(self,name):
        self.name = name
    def show(self):
        print("School Name :-",self.name)

class Student(School):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    def display(self):
        self.show()
        print("Grade :-",self.grade)

s = School("VSHS")
s.show()
ss = Student("NPS",80)
ss.display()
