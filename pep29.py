#add class person and employee
#create a class manager that inherits from both
#add methods to show personal info and job info
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_personal_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class employee:
    def __init__(self, emp_id, position):
        self.emp_id = emp_id
        self.position = position

    def show_job_info(self):
        print(f"Employee ID: {self.emp_id}, Position: {self.position}")

class manager(person, employee):
    def __init__(self, name, age, emp_id, position):
        person.__init__(self, name, age)
        employee.__init__(self, emp_id, position)
    def show_info(self):
        self.show_personal_info()
        self.show_job_info()

m=manager("Alice", 35, "MGR123", "Sales Manager")
m.show_info()   

#create classes camera and phone
#create a class smaartphone that can take pictures and make calls
class camera:
    def take_picture(self):
        print("Picture taken")

class phone:
    def make_call(self, number):
        print(f"Calling {number}...")

class smartphone(camera, phone):
    pass    
s=smartphone()
s.take_picture()
s.make_call("123-456-7890") 

#create classes engine and wheels
#create a class car that can start the engine and move using wheels
class engine:
    def start_engine(self):
        print("Engine started")     

class wheels:
    def move(self):
        print("Car is moving")

class car(engine, wheels):
    pass
c=car()
c.start_engine()
c.move()


#creatre classes teacher and researcher
#create a class professor that can teach and conduct research
class teacher:
    def teach(self, subject):
        print(f"Teaching {subject}")        
class researcher:
    def conduct_research(self, topic):
        print(f"Conducting research on {topic}")
class professor(teacher, researcher):
    pass
p=professor()
p.teach("Mathematics")
p.conduct_research("Quantum Physics")

#create classes battery and screen
#create a class laptop that can provide power and display content
class battery:
    def provide_power(self):
        print("Powering on the device")
class screen:
    def display_content(self, content):
        print(f"Displaying: {content}")
class laptop(battery, screen):
    pass
l=laptop()
l.provide_power()
l.display_content("To kaise hai ap log")