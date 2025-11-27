#1 this accepts and stores and prits an table for a parking system 
parking_data = []
class Car:
    def __init__(self, plate_number, owner_name,model, year):
        self.plate_number = plate_number
        self.owner = owner_name
        self.model = model
        self.year = year
while True:
    plate_number = input("Enter the car's plate number: ")
    owner_name = input("Enter the owner's name: ")
    model = input("Enter the car model: ")
    year = input("Enter the car year: ")

    parking_data.append(Car(plate_number, owner_name, model, year))
 
    again = input("Do you want to add another car? (yes/no): ")
    if again.lower() != 'yes':
        break

print("\nParking System Data:")
print(f"{'Plate Number':<15}{'Owner Name':<20}{'Model':<15}{'Year':<10}")
for car in parking_data:
    print(f"{car.plate_number:<15}{car.owner:<20}{car.model:<15}{car.year:<10}")
#2 this example show how relationships work in classes
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class car:
     def __init__(self, plate_number, model,make):
         self.plate_number = plate_number
         self.model = model
         self.make=make

person1 = person("Alice", 30)
person2 = person("Bob", 25)
car1 = car("ABC123", "Toyota", "2020")
car2 = car("XYZ789", "Honda", "2019")

person1.car = car1
person2.car = car2
print(f"{person1.name} drives a toyota{car1.model} with plate number {car1.plate_number}.")
print(f"{person2.name} drives a honda {car2.model} with plate number {car2.plate_number}.")
#3 add books stores them and lists them 
library = []
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

while True:
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the publication year: ")
   
    library.append(Book(title, author, year))
    again = input("Do you want to add another book? (yes/no): ")
    if again.lower() != 'yes':
        break

    print("\nLibrary Book List:")
    print(f"{'Title':<30}{'Author':<20}{'Year':<10}")
    for book in library:
        print(f"{book.title:<30}{book.author:<20}{book.year:<10}")
#4 registration system 
registrations=[]
class student:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
while True:
        name=input("Enter student name: ")
        id=input("Enter student ID: ")          
        department=input("Enter student department: ")

        registrations.append(student(name,id,department))
        again=input("Do you want to add another student? (yes/no): ")
        if again.lower() !='yes':
            break
print("\nRegistered Students:")
print(f"{'Name':<20}{'ID':<15}{'Department':<20}")
for stud in registrations:
    print(f"{stud.name:<20}{stud.id:<15}{stud.department:<20}")
#5 this is a simple inventory system
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
class Store:
    def __init__(self):
        self.inventory = []
    def add_product(self, product):
        self.inventory.append(product)
    def display_inventory(self):
        print(f"{'Product Name':<20}{'Price':<10}{'Quantity':<10}")
        for product in self.inventory:
            print(f"{product.name:<20}{product.price:<10}{product.quantity:<10}")
store = Store()
while True:
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    store.add_product(Product(name, price, quantity))

    again = input("Do you want to add another product? (yes/no): ")
    if again.lower() != 'yes':
        break

store.display_inventory() 