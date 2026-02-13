# 1. Create a base class University. Derive Student and Teacher from it. # Then create TeachingAssistant that inherits from both Student and Teacher # and implements methods for studying, teaching, and assisting.
# class University:
#     def university_info(self):
#         print("University environment")
# class Student(University):
#     def study(self):
#         print("Student is studying")
# class Teacher(University):
#     def teach(self):
#         print("Teacher is teaching")
# class TeachingAssistant(Student, Teacher):
#     def assist(self):
#         print("Teaching Assistant is assisting students")
# ta = TeachingAssistant()
# ta.study()
# ta.teach()
# ta.assist()

# 2. Create a base class Vehicle. Derive Car and Boat from it. # Then create AmphibiousVehicle that inherits from both Car and Boat # and shows land and water transportation.
# class Vehicle:
#     def show(self):
#         print("This is vehicle")
# class Car(Vehicle):
#     def info(self):
#         print("This is car")
# class Boat(Vehicle):
#     def display(self):
#         print("This is Boat")
# class AmphibiousVehicle(Car, Boat):
#     def wow(self):
#         print("This is AmphibiousVehicle")
# av = AmphibiousVehicle()
# av.wow()
# av.display()
# av.info()
# av.show()

# 3. Create a base class Device. Derive Camera and Phone from it. # Then create SmartGadget that inherits from both Camera and Phone # and performs multitasking operations.
# class Device:
#     def dikhao(self):
#         print("This is Device")
# class Camera(Device):
#     def show(self):
#         print("This is Camera")
# class Phone(Device):
#     def display(self):
#         print("This is Phone")
# class SmartGadget(Camera,Phone):
#     def info(self):
#         print("This is SmartGadget")
# sg = SmartGadget()
# sg.info()
# sg.display()
# sg.show()
# sg.dikhao()

# 4. Create a base class Person. Derive Dancer and Singer from it. # Then create Performer that inherits from both Dancer and Singer # and performs on stage.
# class Person:
#     def show(self):
#         print("This is a Person")
# class Dancer(Person):
#     def info(self):
#         print("This is a Dancer")
# class Singer(Person):
#     def display(self):
#         print("This is a Singer")
# class Performer(Dancer,Singer):
#     def dikhao(self):
#         print("This is a Performer")
# p = Performer()
# p.dikhao()
# p.display()
# p.info()
# p.show()

# 5. Create a base class Company. Derive Programmer and Tester from it. # Then create SoftwareEngineer that inherits from both Programmer and Tester # and handles complete software development.
# class Company:
#     def show(self):
#         print("This is Company")
# class Programmer(Company):
#     def info(self):
#         print("This is Programmer")
# class Tester(Company):
#     def display(self):
#         print("This is Tester")
# class SoftwareEngineer(Programmer,Tester):
#     def dikhao(self):
#         print("This is SoftwareEngineer")
# p = SoftwareEngineer()
# p.dikhao()
# p.display()
# p.info()
# p.show()

# 6. Create a base class Bank. Derive SavingsAccount and LoanAccount from it. # Then create Customer that inherits from both SavingsAccount and LoanAccount # and manages finances.
# class Bank:
#     def show(self):
#         print("This is Bank")
# class SavingsAccount(Bank):
#     def info(self):
#         print("This is SavingsAccount")
# class LoanAccount(Bank):
#     def display(self):
#         print("This is LoanAccount")
# class Customer(SavingsAccount,LoanAccount):
#     def dikhao(self):
#         print("This is Customer")
# p = Customer()
# p.dikhao()
# p.display()
# p.info()
# p.show()

# 7. Create a base class Media. Derive Audio and Video from it. # Then create Multimedia that inherits from both Audio and Video # and plays all types of media.
# class Media:
#     def show(self):
#         print("This is Media")
# class Audio(Media):
#     def info(self):
#         print("This is Audio")
# class Video(Media):
#     def display(self):
#         print("This is Video")
# class Multimedia(Audio,Video):
#     def dikhao(self):
#         print("This is Multimedia")
# p = Multimedia()
# p.dikhao()
# p.display()
# p.info()
# p.show()

# 8. Create a base class School. Derive SportsStudent and MusicStudent from it. # Then create AllRounder that inherits from both SportsStudent and MusicStudent # and performs multiple talents.
# class School:
#     def show(self):
#         print("This is School")
# class SportsStudent(School):
#     def info(self):
#         print("This is SportsStudent")
# class MusicStudent(School):
#     def display(self):
#         print("This is MusicStudent")
# class AllRounder(SportsStudent,MusicStudent):
#     def dikhao(self):
#         self.display()
#         self.info()
# p = AllRounder()
# p.dikhao()
# p.show()

# 9. Create a base class OnlinePlatform. Derive Buyer and Seller from it. # Then create MarketplaceUser that inherits from both Buyer and Seller # and performs trading
# class OnlinePlatform:
#     def show(self):
#         print("This is OnlinePlatform")
# class Buyer(OnlinePlatform):
#     def info(self):
#         print("This is Buyer")
# class Seller(OnlinePlatform):
#     def display(self):
#         print("This is Video")
# class MarketplaceUser(Seller,Buyer):
#     def dikhao(self):
#         print("This is MarketplaceUser")
# p = MarketplaceUser()
# p.dikhao()
# p.display()
# p.info()
# p.show()

# 10. Create a base class Transport. Derive BusService and TrainService from it. # Then create SmartTransport that inherits from both BusService and TrainService # and controls both services.
# class Transport:
#     def show(self):
#         print("This is Transport")
# class BusService(Transport):
#     def info(self):
#         print("This is BusService")
# class TrainService(Transport):
#     def display(self):
#         print("This is TrainService")
# class SmartTransport(TrainService,BusService):
#     def dikhao(self):
#         print("This is SmartTransport")
# p = SmartTransport()
# p.dikhao()
# p.display()
# p.info()
# p.show()
