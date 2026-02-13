# 1. Create a Student class where marks are private and accessed using getter method
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks
# s = Student('Abir',100)
# print(s.get_marks())


# 2. Create a BankAccount class with private balance and methods to deposit and check balance.
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance
# s = BankAccount(1000)
# print(s.get_balance())

# 3. Create a Person class where age is private and cannot be negative.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.set_age(age)

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         if age < 0:
#             raise ValueError("Age cannot be negative")
#         self.__age = age
# p1 = Person("Bob", 30)
# print(p1.name)
# print(p1.get_age())

# 4. Create a User class that hides password and verifies it using a method.
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password

#     def verify_password(self, input_password):
#         return self.__password == input_password
# user1 = User("alice", "secret123")
# print(user1.verify_password("secret123"))
# print(user1.verify_password("wrongpass"))

# 5. Create an Employee class where salary is private and can be increased.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#     def get_salary(self):
#         return self.__salary
#     def increase_salary(self, amount):
#         if amount <= 0:
#             raise ValueError("Increase amount must be positive")
#         self.__salary += amount
# emp = Employee("John", 50000)
# print(f"Initial salary: {emp.get_salary()}")
# emp.increase_salary(5000)
# print(f"New salary: {emp.get_salary()}")
# try:
#     emp.increase_salary(-100)
# except ValueError as e:
#     print(e)


# 6. Create a Car class with private speed and methods accelerate and brake.
# class Car:
#     def __init__(self, max_speed=200):
#         self.__speed = 0
#         self.__max_speed = max_speed
#     def get_speed(self):
#         return self.__speed
#     def accelerate(self, increment):
#         if increment <= 0:
#             raise ValueError("Acceleration must be positive")
#         new_speed = self.__speed + increment
#         self.__speed = min(new_speed, self.__max_speed)
#     def brake(self, decrement):
#         if decrement <= 0:
#             raise ValueError("Braking must be positive")
#         self.__speed = max(0, self.__speed - decrement)
# car = Car(180)
# print(f"Current speed: {car.get_speed()}")
# car.accelerate(50)
# print(f"After accelerate: {car.get_speed()}")

# 7. Create a Mobile class where battery percentage is private and decreases when used.
# class Mobile:
#     def __init__(self, initial_battery=100):
#         if initial_battery < 0 or initial_battery > 100:
#             raise ValueError("Battery must be between 0-100%")
#         self.__battery = initial_battery
#     def get_battery(self):
#         return self.__battery
#     def make_call(self, duration_minutes):
#         battery_drain = duration_minutes * 1
#         self.__battery = max(0, self.__battery - battery_drain)

#     def browse_internet(self, time_minutes):
#         battery_drain = time_minutes * 2
#         self.__battery = max(0, self.__battery - battery_drain)
#     def charge(self, percentage):
#         if percentage <= 0:
#             raise ValueError("Charge amount must be positive")
#         self.__battery = min(100, self.__battery + percentage)
# phone = Mobile(80)
# print(f"Initial battery: {phone.get_battery()}%")
# phone.make_call(10)
# print(f"After 10min call: {phone.get_battery()}%")

# 8. Create an ATM class with hidden PIN and verification method.
# class ATM:
#     def __init__(self, account_number, pin):
#         self.account_number = account_number
#         self.__pin = pin
#         self.__balance = 1000.0
#         self.__is_authenticated = False

#     def verify_pin(self, entered_pin):
#         self.__is_authenticated = (self.__pin == entered_pin)
#         return self.__is_authenticated

#     def check_balance(self):
#         if not self.__is_authenticated:
#             return "Please verify PIN first"
#         return f"Balance: ${self.__balance:.2f}"

#     def withdraw(self, amount):
#         if not self.__is_authenticated:
#             return "Please verify PIN first"
#         if amount <= 0 or amount > self.__balance:
#             return "Invalid amount"
#         self.__balance -= amount
#         return f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}"

#     def deposit(self, amount):
#         if not self.__is_authenticated:
#             return "Please verify PIN first"
#         if amount <= 0:
#             return "Invalid amount"
#         self.__balance += amount
#         return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"
# atm = ATM("123456", "7890")
# print(atm.check_balance())  # Output: Please verify PIN first
# if atm.verify_pin("7890"):
#     print("PIN verified")
# else:
#     print("Wrong PIN")
# print(atm.check_balance())      # Output: Balance: $1000.00
# print(atm.withdraw(200))        # Output: Withdrew $200.00. New balance: $800.00
# print(atm.deposit(150))         # Output: Deposited $150.00. New balance: $950.00
# atm.verify_pin("0000")  # Wrong PIN
# print(atm.withdraw(100))  # Output: Please verify PIN first

# 9. Create a Book class where price is private and cannot be negative.
# class Book:
#     def __init__(self, title, price):
#         self.title = title
#         self.set_price(price)
#     def get_price(self):
#         return self.__price
#     def set_price(self, price):
#         if price < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = price
# book1 = Book("Python Basics", 29.99)
# print(f"{book1.title}: ${book1.get_price()}")
# book1.set_price(34.99)
# print(f"New price: ${book1.get_price()}")
# try:
#     book2 = Book("Invalid Book", -10)
# except ValueError as e:
#     print(e)

# 10. Create a Result class where marks list is private and modified using methods.
class Result:
    def __init__(self, marks):
        self.__marks = marks[:]
    def get_marks(self):
        return self.__marks[:]

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.__marks.append(mark)
        else:
            raise ValueError("Mark must be between 0-100")
    def update_mark(self, index, new_mark):
        if index < 0 or index >= len(self.__marks):
            raise IndexError("Invalid index")
        if 0 <= new_mark <= 100:
            self.__marks[index] = new_mark
        else:
            raise ValueError("Mark must be between 0-100")
    def remove_mark(self, index):
        if index < 0 or index >= len(self.__marks):
            raise IndexError("Invalid index")
        return self.__marks.pop(index)
    def get_average(self):
        return sum(self.__marks) / len(self.__marks) if self.__marks else 0
r = Result([1,100,60])
print(r.get_marks())
print(r.get_average())
r.add_mark(90)
print(r.get_marks())
r.update_mark(0,30)
print(r.get_marks())
r.remove_mark(2)
print(r.get_marks())
