#1 this accepts and stores and prits an table for a parking system 
parking_data = []
class Car:
    def __init__(self, plate_number, owner_name,model, year):
        self.plate_number = plate_number
        self.owner = owner_name
        self.model = model
        self.year = year
   
plate_number = input("Enter the car's plate number: ")
owner_name = input("Enter the owner's name: ")
model = input("Enter the car model: ")
year = input("Enter the car year: ")

parking_data.append(Car(plate_number, owner_name, model, year))

print("\nParking System Data:")
print(f"{'Plate Number':<15}{'Owner Name':<20}{'Model':<15}{'Year':<10}")
for car in parking_data:
    print(f"{car.plate_number:<15}{car.owner:<20}{car.model:<15}{car.year:<10}")