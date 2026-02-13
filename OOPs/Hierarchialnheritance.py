# class RollsRoyce:
#     def __init__(self,engine,comfort):
#         self.engine = engine
#         self.comfort = comfort
#     def show(self):
#         print("Engine :-",self.engine)
#         print("Comfort :-",self.comfort)
# class BMW(RollsRoyce):
#     def __init__(self, engine,comfort):
#         super().__init__(engine,comfort)
#     def info(self):
#         print("BMW deriving engine from RR",self.engine)
# class VW(RollsRoyce):
#     def __init__(self, engine, comfort):
#         super().__init__(engine, comfort)
#     def display(self):
#         print("VW deriving comfort from RR",self.comfort)
# vw = VW(1200,"Good")
# vw.display()

#Q1. Create a parent class Payment and child classes UPI, CreditCard, and Cash. Implement a method in Payment to pay amount and specific methods in each child for payment type
# Parent class
# class Payment:
#     def pay_amount(self, amount):
#         print(f"Paying ₹{amount}")
# class UPI(Payment):
#     def upi_payment(self, amount):
#         self.pay_amount(amount)
#         print("Payment done using UPI")
# class CreditCard(Payment):
#     def card_payment(self, amount):
#         self.pay_amount(amount)
#         print("Payment done using Credit Card")
# class Cash(Payment):
#     def cash_payment(self, amount):
#         self.pay_amount(amount)
#         print("Payment done using Cash")

# u = UPI()
# u.upi_payment(500)
# c = CreditCard()
# c.card_payment(1200)
# ca = Cash()
# ca.cash_payment(300)

# 2. Create a parent class Notification and child classes Email, SMS, and Push. Implement a general send method and specific send methods for each notification type.
# class Notification:
#     def send(self):
#         print("Notification send through :-",self.mess)
# class Email(Notification):
#     def __init__(self,mess):
#         self.mess = mess
#         self.send()
# class SMS(Notification):
#     def __init__(self,mess):
#         self.mess = mess
#         self.send()
# class Push(Notification):
#     def __init__(self,mess):
#         self.mess = mess
#         self.send()
# e = Email("Email")
# s = Email("SMS")
# p = Email("Push")

#Q3. Create a parent class Exam and child classes OnlineExam and OfflineExam. Add functionality for starting the exam and special features for each exam mode.
# class Exam:
#     def info(self):
#         print("Mode of Examination :-",self.mode)
# class OnlineExam(Exam):
#     def __init__(self,mode):
#         self.mode = mode
#         super().info()
# class OfflineExam(Exam):
#     def __init__(self,mode):
#         self.mode = mode
#         super().info()
# e = OfflineExam("Offline")
# o = OnlineExam("Online")

#Q4.Create a parent class Transport and child classes Train, Flight, and Ship. Implement common travel method and specialized travel methods for each transport type.
# class Transport:
#     def mode(self):
#         print("Mode of Transport :-",self.method)
# class Train(Transport):
#     def __init__(self,method):
#         self.method = method
#         self.mode()
# class Flight(Transport):
#     def __init__(self,method):
#         self.method = method
#         self.mode()
# class Ship(Transport):
#     def __init__(self,method):
#         self.method = method
#         self.mode()
# t = Train("Train")
# f = Flight("Flight")
# s = Ship("Ship")

#Q5.Create a parent class Employee and child classes HR, Engineer, and Sales. Implement attendance functionality and specific job-related methods in each child.
# Parent class
# class Employee:
#     def __init__(self, name):
#         self.name = name
#     def attendance(self):
#         print(self.name, "has marked attendance")
# class HR(Employee):
#     def manage_recruitment(self):
#         print(self.name, "is managing recruitment")
# class Engineer(Employee):
#     def develop_software(self):
#         print(self.name, "is developing software")
# class Sales(Employee):
#     def sell_products(self):
#         print(self.name, "is selling products")
# hr = HR("Amit")
# eng = Engineer("Riya")
# sale = Sales("Rahul")
# hr.attendance()
# hr.manage_recruitment()
# eng.attendance()
# eng.develop_software()
# sale.attendance()
# sale.sell_products()

#Q6.Create a parent class Order and child classes FoodOrder, GroceryOrder, and MedicineOrder. Add order placement method and specialized processing methods for each order type.
# class Order:
#     def type(self):
#         print("Type of Order :-",self.order)
# class FoodOrder(Order):
#     def __init__(self,order):
#         self.order = order
#         self.type()
# class GroceryOrder(Order):
#     def __init__(self,order):
#         self.order = order
#         self.type()
# class MedicineOrder(Order):
#     def __init__(self,order):
#         self.order = order
#         self.type()
# fo = FoodOrder("FoodOrder")
# go = FoodOrder("GroceryOrder")
# mo = FoodOrder("MedicineOrder")

#Q7. Create a parent class Content and child classes Blog, Video, and Podcast. Implement content publishing and specialized creation methods in each content type.
# Parent class
# class Content:
#     def __init__(self, title):
#         self.title = title
#     def publish(self):
#         print(f"Publishing content: {self.title}")
# class Blog(Content):
#     def write_blog(self):
#         print(f"Writing blog titled '{self.title}'")
# class Video(Content):
#     def record_video(self):
#         print(f"Recording video titled '{self.title}'")
# class Podcast(Content):
#     def record_podcast(self):
#         print(f"Recording podcast titled '{self.title}'")
# b = Blog("Python OOP Basics")
# b.publish()
# b.write_blog()
# v = Video("Django Tutorial")
# v.publish()
# v.record_video()
# p = Podcast("Tech Talk Episode 1")
# p.publish()
# p.record_podcast()

# 8. Create a parent class Ticket and child classes MovieTicket, BusTicket, and FlightTicket. Add ticket booking functionality and special booking details for each ticket type.
# Parent class
# class Ticket:
#     def __init__(self, ticket_no):
#         self.ticket_no = ticket_no
#     def book_ticket(self):
#         print(f"Ticket {self.ticket_no} booked successfully")
# class MovieTicket(Ticket):
#     def movie_details(self, movie_name, seat):
#         print(f"Movie: {movie_name}, Seat: {seat}")
# class BusTicket(Ticket):
#     def bus_details(self, route, seat):
#         print(f"Route: {route}, Seat: {seat}")
# class FlightTicket(Ticket):
#     def flight_details(self, flight_name, seat):
#         print(f"Flight: {flight_name}, Seat: {seat}")
# m = MovieTicket(101)
# m.book_ticket()
# m.movie_details("Inception", "A10")
# b = BusTicket(202)
# b.book_ticket()
# b.bus_details("Delhi to Jaipur", "12")
# f = FlightTicket(303)
# f.book_ticket()
# f.flight_details("AI-202", "18C")

#Q9. Create a parent class File and child classes PDF, ImageFile, and AudioFile. Implement file opening method and specialized actions for each file type.
# Parent class
# class File:
#     def __init__(self, filename):
#         self.filename = filename
#     def open_file(self):
#         print(f"Opening file: {self.filename}")
# class PDF(File):
#     def read_pdf(self):
#         print(f"Reading PDF file: {self.filename}")
# class ImageFile(File):
#     def view_image(self):
#         print(f"Viewing image file: {self.filename}")
# class AudioFile(File):
#     def play_audio(self):
#         print(f"Playing audio file: {self.filename}")
# p = PDF("notes.pdf")
# i = ImageFile("photo.jpg")
# a = AudioFile("song.mp3")
# p.open_file()
# p.read_pdf()
# i.open_file()
# i.view_image()
# a.open_file()
# a.play_audio()

# 10. Create a parent class Service and child classes Cleaning, Repair, and Delivery. Implement service request functionality and specialized service methods for each service type
# Parent class
class Service:
    def __init__(self, service_id):
        self.service_id = service_id
    def request_service(self):
        print(f"Service ID {self.service_id} has been requested")
class Cleaning(Service):
    def clean_area(self, area):
        print(f"Cleaning service for {area}")
class Repair(Service):
    def repair_item(self, item):
        print(f"Repair service for {item}")
class Delivery(Service):
    def deliver_item(self, item, address):
        print(f"Delivering {item} to {address}")
c = Cleaning(1)
r = Repair(2)
d = Delivery(3)
c.request_service()
c.clean_area("Office")
r.request_service()
r.repair_item("Laptop")
d.request_service()
d.deliver_item("Package", "New Delhi")
