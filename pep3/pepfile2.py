#Create a base class University. Derive Student and Teacher from it. 
#Then create TeachingAssistant that inherits from both Student and Teacher 
#and implements methods for studying, teaching, and assisting.
class University:
    def info(self):
        print("Welcome to the University")
class Student(University):
    def study(self, subject):
        print(f"Studying {subject}")    
class Teacher(University):
    def teach(self, subject):
        print(f"Teaching {subject}")
class TeachingAssistant(Student, Teacher):
    def assist(self, subject):
        print(f"Assisting in {subject}\n")
ta = TeachingAssistant()
ta.info()   
ta.study("Mathematics")
ta.teach("Physics")
ta.assist("Chemistry\n")

#Create a base class Vehicle. Derive Car and Boat from it. 
#Then create AmphibiousVehicle that inherits from both Car and Boat 
#and shows land and water transportation.
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def drive(self):
        print("Driving on land")

class Boat(Vehicle):
    def sail(self):
        print("Sailing on water")

class AmphibiousVehicle(Car, Boat):
    def transport(self):
        print("Transporting on land and water\n")

av = AmphibiousVehicle()
av.info()
av.drive()
av.sail()
av.transport()

#Create a base class Device. Derive Camera and Phone from it. 
#Then create SmartGadget that inherits from both Camera and Phone 
#and performs multitasking operations.
class device:
    def info(self):
        print("these are smart devices")
class camera(device):
    def click(self):
        print("this is a camera")
class phone(device):
    def use(self):
        print("this is a smartphone")
class smartgadget(camera,phone):
    def gadgets(self):
        print("clicking through the camera and storing in the phone")

d=smartgadget()
d.info()
d.click()
d.use()
d.gadgets()

#Create a base class Person. Derive Dancer and Singer from it. 
#Then create Performer that inherits from both Dancer and Singer 
#and performs on stage.
class person:
    def info(self):
        print("This is a person")
class dancer(person):
    def dance(self):
        print("Dancing on stage")
class singer(person):
    def sing(self):
        print("Singing on stage")
class performer(dancer,singer):
    def perform(self):
        print("Performing dance and song on stage\n")
p=performer()
p.info()
p.dance()
p.sing()
p.perform()

#Create a base class Company. Derive Programmer and Tester from it. 
#Then create SoftwareEngineer that inherits from both Programmer and Tester 
#and handles complete software development.
class company:
    def info(self):
        print("This is a company")
class programmer(company):
    def code(self):
        print("Writing code")
class tester(company):
    def test(self):
        print("Testing software")
class softwareengineer(programmer,tester):
    def develop(self):
        print("Handling complete software development\n")
se=softwareengineer()
se.info()
se.code()
se.test()
se.develop()

#Create a base class Bank. Derive SavingsAccount and LoanAccount from it. 
#Then create Customer that inherits from both SavingsAccount and LoanAccount 
#and manages finances.
class bank:
    def info(self):
        print("This is a bank")
class savingsaccount(bank):
    def save(self):
        print("Saving money")
class loanaccount(bank):
    def borrow(self):
        print("Borrowing money")
class customer(savingsaccount,loanaccount):
    def manage(self):
        print("Managing finances\n")
c=customer()
c.info()
c.save()
c.borrow()
c.manage()  

#Create a base class Media. Derive Audio and Video from it. 
#Then create Multimedia that inherits from both Audio and Video 
#and plays all types of media.
class media:
    def info(self):
        print("This is a media")
class audio(media):
    def play_audio(self):
        print("Playing audio")
class video(media):
    def play_video(self):
        print("Playing video")
class multimedia(audio,video):
    def play_all(self):
        print("Playing all types of media\n")       
mm=multimedia()
mm.info()
mm.play_audio()
mm.play_video()
mm.play_all()   

#Create a base class School. Derive SportsStudent and MusicStudent from it. 
#Then create AllRounder that inherits from both SportsStudent and MusicStudent 
#and performs multiple talents.
class school:
    def info(self):
        print("This is a school")
class sportsstudent(school):
    def play_sport(self):
        print("Playing sports")
class musicstudent(school):
    def play_music(self):
        print("Playing music")
class allrounder(sportsstudent,musicstudent):
    def perform(self):
        print("Performing multiple talents\n")
ar=allrounder()
ar.info()
ar.play_sport()
ar.play_music()
ar.perform()

# 9. Create a base class OnlinePlatform. Derive Buyer and Seller from it. 
#    Then create MarketplaceUser that inherits from both Buyer and Seller 
#    and performs trading.
class onlineplatform:
    def info(self):
        print("This is an online platform")
class buyer(onlineplatform):
    def buy(self):
        print("Buying products")
class seller(onlineplatform):
    def sell(self):
        print("Selling products")
class marketplaceuser(buyer,seller):
    def trade(self):
        print("Performing trading activities\n")
mu=marketplaceuser()
mu.info()
mu.buy()
mu.sell()
mu.trade()

#Create a base class Transport. Derive BusService and TrainService from it. 
#Then create SmartTransport that inherits from both BusService and TrainService 
#and controls both services.
class transport:
    def info(self):
        print("This is a transport service")
class busservice(transport):
    def bus_info(self):
        print("This is a bus service")
class trainservice(transport):
    def train_info(self):
        print("This is a train service")
class smarttransport(busservice,trainservice):
    def control_services(self):
        print("Controlling both bus and train services\n")
st=smarttransport()
st.info()
st.bus_info()
st.train_info()
st.control_services()
