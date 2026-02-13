#hierarchial inheritance
#create a parent class payment and child classes upi, creditcard, cash
#implement a method in paymentto pay amount and specific methods in each child for payment type
class Payment:
    def pay(self, amount):
        print(f"Paying amount: {amount}")
class UPI(Payment):
    def pay_via_upi(self, upi_id, amount):
        self.pay(amount)
        print(f"Paid {amount} via UPI ID: {upi_id}")
class CreditCard(Payment):
    def pay_via_credit_card(self, card_number, amount):
        self.pay(amount)
        print(f"Paid {amount} via Credit Card: {card_number}")
class Cash(Payment):
    def pay_via_cash(self, amount):
        self.pay(amount)
        print(f"Paid {amount} in Cash\n")

upi_payment = UPI()
upi_payment.pay_via_upi("user@bank", 500)   
credit_payment = CreditCard()
credit_payment.pay_via_credit_card("1234-5678-9012-3456", 1000)   
cash_payment = Cash()
cash_payment.pay_via_cash(200)

#create a parent class notification and child classes email, sms and push.
#implement a general send methods and specific send methods in each notification type
class notification:
    def tingting(self):
        print("notifications were sent successfully")
class email(notification):
    def tingting_email(self):
        print("email was sent successfully")
class sms(notification):
    def tingting_sms(self):
        print("sms was sent successfully")
class push(notification):
    def tingting_push(self):
        print("your message was pushed successfully\n")

n = notification()
n.tingting()
e = email()
e.tingting_email()
s = sms()
s.tingting_sms()
p = push()
p.tingting_push()

#create parent class exam and child class onlineexam and offlineexam
#add functionality for starting the exam and special features 
class exam():
    def start_exam(self):
        print("Exam has started")
class onlineexam(exam):
    def start_online_exam(self):
        print("Online exam started with proctoring")
class offlineexam(exam):
    def start_offline_exam(self):
        print("Offline exam started in the exam hall\n")  

oe = onlineexam()
oe.start_exam() 
oe.start_online_exam()
ofe = offlineexam()
ofe.start_exam()
ofe.start_offline_exam()    

#create a parent class transport and cild classes train,flight and ship
#implement common travel methodand specialized methods for each transport type
class transport():
    def __init__(self,destination):
        self.destination=destination
    def travel(self):
        print(f"Traveling to {self.destination}")
class train(transport):
    def travel_by_train(self):
        print(f"Traveling to {self.destination} by train")
class flight(transport):
    def travel_by_flight(self):
        print(f"Traveling to {self.destination} by flight")
class ship(transport):
    def travel_by_ship(self):
        print(f"Traveling to {self.destination} by ship\n")       

t1 = train("New York")
t1.travel()
t1.travel_by_train()
f1 = flight("London")
f1.travel()
f1.travel_by_flight()
s1 = ship("Sydney")
s1.travel()
s1.travel_by_ship()

#create a parent class employee and child classes hr,engineer and sales
#implement attendance functionality and specific job related methods in each child
class Employee:
    def mark_attendance(self):
        print("Attendance marked")
class HR(Employee):
    def conduct_interview(self, candidate_name):
        print(f"Conducting interview for {candidate_name}")
class Engineer(Employee):
    def develop_software(self, software_name):
        print(f"Developing software: {software_name}")
class Sales(Employee):
    def make_sale(self, product_name):
        print(f"Making sale of product: {product_name}\n")

hr_emp = HR()
hr_emp.mark_attendance()
hr_emp.conduct_interview("Alice")

eng_emp = Engineer()
eng_emp.mark_attendance()
eng_emp.develop_software("Inventory Management System")

sales_emp = Sales()
sales_emp.mark_attendance()
sales_emp.make_sale("Laptop")

#Create a parent class Order and child classes FoodOrder, GroceryOrder, and MedicineOrder. 
#Add order placement method and specialized processing methods for each order type.
class Order:
    def place_order(self, order_id):
        print(f"Order {order_id} has been placed")
class FoodOrder(Order):
    def process_food_order(self, order_id):
        print(f"Processing food order {order_id}")
class GroceryOrder(Order):
    def process_grocery_order(self, order_id):
        print(f"Processing grocery order {order_id}")
class MedicineOrder(Order):
    def process_medicine_order(self, order_id):
        print(f"Processing medicine order {order_id}\n")


mo = MedicineOrder()
mo.place_order("M123")
mo.process_medicine_order("M123")
fo = FoodOrder()
fo.place_order("F456")
fo.process_food_order("F456")
go = GroceryOrder()
go.place_order("G789")
go.process_grocery_order("G789")

#Create a parent class Content and child classes Blog, Video, and Podcast. 
#Implement content publishing and specialized creation methods in each content type.
class Content:
    def publish(self, title):
        print(f"Publishing content: {title}")
class Blog(Content):
    def create_blog(self, title):
        print(f"Creating blog post: {title}")
class Video(Content):
    def create_video(self, title):
        print(f"Creating video: {title}")
class Podcast(Content):
    def create_podcast(self, title):
        print(f"Creating podcast episode: {title}\n")

blog = Blog()
blog.publish("My First Blog")
blog.create_blog("My First Blog")
video = Video()
video.publish("My First Video")
video.create_video("My First Video")
podcast = Podcast()
podcast.publish("My First Podcast")
podcast.create_podcast("My First Podcast")

#Create a parent class Ticket and child classes MovieTicket, BusTicket, and FlightTicket. 
#Add ticket booking functionality and special booking details for each ticket type.
class Ticket:
    def book_ticket(self, ticket_id):
        print(f"Ticket {ticket_id} has been booked")
class MovieTicket(Ticket):
    def book_movie_ticket(self, ticket_id):
        print(f"Booking movie ticket {ticket_id}")
class BusTicket(Ticket):
    def book_bus_ticket(self, ticket_id):
        print(f"Booking bus ticket {ticket_id}")
class FlightTicket(Ticket):
    def book_flight_ticket(self, ticket_id):
        print(f"Booking flight ticket {ticket_id}\n")

mt = MovieTicket()
mt.book_ticket("MT001")
mt.book_movie_ticket("MT001")
bt = BusTicket()
bt.book_ticket("BT002")
bt.book_bus_ticket("BT002")
ft = FlightTicket()
ft.book_ticket("FT003")
ft.book_flight_ticket("FT003")  

#Create a parent class File and child classes PDF, ImageFile, and AudioFile. 
#Implement file opening method and specialized actions for each file type.
class File:
    def open_file(self, file_name):
        print(f"Opening file: {file_name}")
class PDF(File):
    def read_pdf(self, file_name):
        print(f"Reading PDF file: {file_name}")
class ImageFile(File):
    def view_image(self, file_name):
        print(f"Viewing image file: {file_name}")
class AudioFile(File):
    def play_audio(self, file_name):
        print(f"Playing audio file: {file_name}\n")

pdf = PDF()
pdf.open_file("document.pdf")
pdf.read_pdf("document.pdf")
image = ImageFile()
image.open_file("picture.jpg")
image.view_image("picture.jpg")
audio = AudioFile()
audio.open_file("song.mp3")
audio.play_audio("song.mp3")

#Create a parent class Service and child classes Cleaning, Repair, and Delivery. 
#Implement service request functionality and specialized service methods for each service type.
class Service:
    def request_service(self, service_type):
        print(f"Requesting service: {service_type}")
class Cleaning(Service):
    def schedule_cleaning(self, date):
        print(f"Scheduling cleaning service on {date}")
class Repair(Service):
    def schedule_repair(self, date):
        print(f"Scheduling repair service on {date}")
class Delivery(Service):
    def schedule_delivery(self, date):
        print(f"Scheduling delivery service on {date}\n")

cleaning_service = Cleaning()
cleaning_service.request_service("Cleaning")
cleaning_service.schedule_cleaning("2024-07-01")
repair_service = Repair()
repair_service.request_service("Repair")
repair_service.schedule_repair("2024-07-02")
delivery_service = Delivery()
delivery_service.request_service("Delivery")
delivery_service.schedule_delivery("2024-07-03")