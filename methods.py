#1 THIS SHOWS DIFFERENT METHODS IN A CLASS
class Phone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery   # battery percentage

    def call(self, person):
        print(f"Calling {person}...")
        self.battery -= 5   # using battery
        print(f"Battery now: {self.battery}%")

    def charge(self):
        print("Charging...")
        self.battery = 100
        print(f"Battery now: {self.battery}%")

    def phone_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery: {self.battery}%")
#2 Bank account system to practice methods
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Account balance: ${self.balance}")
#3 this shows a students grade calculation system with methods 
class Student:
    def __init__(self, name):
        self.name = name
        self.list_of_grades = []   # correct safe list

    def add_grade(self, grade):
        self.list_of_grades.append(grade)
        print(f"Grade {grade} added.")

    def calculate_average(self):
        if self.list_of_grades:
            average = sum(self.list_of_grades) / len(self.list_of_grades)
            return average
        else:
            return 0

    def student_info(self):
        print(f"Student Name: {self.name}")
        print(f"Grades: {self.list_of_grades}")
        print(f"Average Grade: {self.calculate_average()}")
