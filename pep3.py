# 1. Create an abstract class Animal with abstract method sound() and implement it in Dog class.
from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("Bark\n")
d=dog()
d.sound()

# 2. Create an abstract class Shape with abstract method area() and implement it in Rectangle class.
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def area(self):
        print("This is a rectangle\n")
r=rectangle()
r.area()

# 3. Create an abstract class Bank with abstract method interest_rate() and implement it in SBI class.
from abc import ABC, abstractmethod
class bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass
class SBI(bank):
    def interest_rate(self,roi):
        print(f"{roi}% interest rate is too high, isnt it?\n")
ir=SBI()
ir.interest_rate(12.45)

# 4. Create an abstract class Vehicle with abstract method speed() and implement it in Car class.
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass
class car(vehicle):
    def speed(self,accn):
        print(f"the car goes vroom vroom at {accn}kmph\n")
c=car()
c.speed(102)

# 5. Create an abstract class Employee with abstract method salary() and implement it in Developer class.
from abc import ABC, abstractmethod
class employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class developer(employee):
    def salary(self,amt):
        print(f"The developer's salary is confidential, but on avg its {amt}lpa\n")
s=developer()
s.salary(18)

# 6. Create an abstract class Payment with abstract method pay(amount) and implement it in UPI class.
from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI\n")
p=UPI()
p.pay(1000)

# 7. Create an abstract class Mobile with abstract method features() and implement it in Samsung class.
from abc import ABC, abstractmethod
class mobile(ABC):
    @abstractmethod
    def features(self):
        pass
class samsung(mobile):
    def features(self,disp,cam):
        print(f"Samsung mobile has great features like AMOLED display of {disp}HZ and good camera of {cam}MP\n")
s=samsung()
s.features(120,108)

# 8. Create an abstract class Course with abstract method duration() and implement it in PythonCourse class.
from abc import ABC, abstractmethod
class course(ABC):
    @abstractmethod
    def duration(self):
        pass
class pythoncourse(course):
    def duration(self,time):
        print(f"the python course went for around {time} hours\n")
d=pythoncourse()
d.duration(3)

# 9. Create an abstract class Food with abstract method price() and implement it in Pizza class.
from abc import ABC, abstractmethod
class food(ABC):
    @abstractmethod
    def price(self):
        pass
class pizza(food):
    def price(self,amt):
        print(f"The price of the pizza is around {amt}rs\n")
p=pizza()
p.price(499)

# 10. Create an abstract class Electronics with abstract method warranty() and implement it in Laptop class.
from abc import ABC, abstractmethod
class electronics(ABC):
    @abstractmethod
    def warranty(self):
        pass
class laptop(electronics):
    def warranty(self,yrs):
        print(f"The laptop comes with a warranty of {yrs} years\n")
w=laptop()
w.warranty(2)