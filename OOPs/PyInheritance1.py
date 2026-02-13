# Step 1: Define a class names 'Car' with attributes# class Car:
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

# my_car = Car("Tata","Sierra",2020)
# print(my_car.make)
# print(my_car.model)
# print(my_car.year)

# class EV(Car):
#     def __init__(self, make,model,year, type):
#         super().__init__(make,model,year)
#         self.type = type
#     def display(self):
#         print(self.make,self.model,self.year,self.type)

# ev = EV("Tata","Sierra",2020,"EV")
# ev.display()
