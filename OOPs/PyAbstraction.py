# Example 1: Shape abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

print(Circle(5).area())


# Example 2: Vehicle abstraction
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car started"

print(Car().start())


# Example 3: Payment abstraction
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

print(CreditCard().pay(2000))


# Example 4: Animal sound abstraction
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

print(Dog().sound())


# Example 5: Bank account abstraction
class Account(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Insufficient balance"

print(SavingsAccount(5000).withdraw(1000))


# Example 6: Appliance abstraction
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        return "Fan is running"

print(Fan().turn_on())


# Example 7: Employee role abstraction
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def salary(self):
        return 60000

print(Developer().salary())


# Example 8: Notification abstraction
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        return f"Email sent: {message}"

print(Email().send("Hello"))


# Example 9: Media player abstraction
class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass

class MP3Player(MediaPlayer):
    def play(self):
        return "Playing MP3"

print(MP3Player().play())


# Example 10: Database abstraction
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        return "Connected to MySQL"

print(MySQL().connect())
