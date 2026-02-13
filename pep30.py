#create a class device that turns on, inherit it into mobile that can make calls
#then inherit mobile into smartphone that can run apps
class device:
    def turn_on(self):
        print("Device is now ON")   
class mobile(device):
    def make_call(self, number):
        print(f"Calling {number}...")
class smartphone(mobile):
    def run_app(self, app_name):
        print(f"Running {app_name} app")
s=smartphone()
s.turn_on()
s.make_call("987-654-3210")
s.run_app("WhatsApp")   

#create class shape, inherit it into rect to calculate area
#then inherit it into coloredrect that adds color info.
class shape:
    def area(self):
        pass
class rect(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class coloredrect(rect):
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color
    def show_info(self):
        print(f"Color: {self.color}, Area: {self.area()}")
cr=coloredrect(5, 10, "Red")
cr.show_info()

#create a class school that displays school name, inherit it into teacher that shows subject
#then inherit it into mathteacher that teaches mathematics
class School:
    def __init__(self, school_name):
        self.school_name = school_name
    def display_school(self):
        print("School:", self.school_name)
class Teacher(School):
    def __init__(self, school_name, subject):
        super().__init__(school_name)
        self.subject = subject
    def display_subject(self):
        print("Subject:", self.subject)
class MathTeacher(Teacher):
    def __init__(self, school_name):
        super().__init__(school_name, "Mathematics")
    def teach(self):
        print("Teaching Mathematics")

m = MathTeacher("LOVELY PROFESSIONAL SCHOOL")
m.display_school()
m.display_subject()
m.teach()

   
