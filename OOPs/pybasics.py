# Create a BankAccount class with deposit and withdraw methods

# class BankAccount:
#     def __init__(self):
#         self.deposit = 0
#         self.withdraw = 0
#         self.balance = 100
#     def checkBalance(self):
#         # self.balance = deposit+withdraw
#         print("Balance :-",self.balance)
#     def deposited(self,deposit):
#         self.balance += deposit
#         print("Balance :-",self.balance)
#     def withdrawed(self,withdraw):
#         self.balance -= withdraw
#         print("Balance :-",self.balance)

# sbi = BankAccount()
# sbi.checkBalance()
# sbi.deposited(100)
# sbi.withdrawed(50)

# Calculate salary with bonus

# class Salary:
#     def __init__(self,salary,bonus):
#         self.salary = salary
#         self.bonus = bonus
#     def addBonus(self,bonus):
#         self.salary += bonus
#         print("Current Salary :-",self.salary)
# emp = Salary(1000,0)
# print(emp.salary)
# print(emp.bonus)
# emp.addBonus(50)

# Track Battery Usage

# class Battery:
#     def __init__(self):
#         self.charge = 10
#         self.degrade = 0
#         self.battery = self.charge+self.degrade
#         print("Current Charge :-",self.battery,"%")
#     def charging(self,charge):
#         self.battery += charge
#         print("Current Charge after Charging:-",self.battery,"%")
#     def discharge(self,degrade):
#         self.battery -= degrade
#         print("Current Charge after Degrading:-",self.battery,"%")
# apple = Battery()
# apple.charging(50)
# apple.discharge(5)

#check book availability

class Book:
    def __init__(self,Book):
        self.book = Book
    def search(self,name):
        if(self.book==name):
            print("Available")
        else:
            print("Not Available")
okok = Book("CSE")
okok.search("ECE")
