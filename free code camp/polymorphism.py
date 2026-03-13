# polymorphism
class Car():
    
    def __init__(self,brand,model,year,number_of_doors,number_of_wheels):
        self.brand=brand
        self.model=model
        self.year=year
        self.number_of_doors=number_of_doors
        self.number_of_wheels=number_of_wheels
        
    def start_car(self):
        print("car is starting")
    def stop_car(self):
        print("car is stopping")

class Bike():
    def __init__(self,brand,model,year,number_of_wheels):
        self.brand=brand
        self.model=model
        self.year=year
        self.number_of_wheels=number_of_wheels

    def start_bike(self):
        print("bike is starting")
    def stop_bike(self):
        print("bike is stopping")

# list of vehicle to inspect
vehicles=[
    Car("Ford","Mustang",2009,4,4),
    Bike("BMW","S100RR",2022,2)

]

for vehicle in vehicles:
    if isinstance(vehicle,Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} of model {vehicle.year} {type(vehicle).__name__}")
        vehicle.start_car()
        vehicle.stop_car()
    elif isinstance(vehicle,Bike):
        print(f"Inspecting {vehicle.brand} {vehicle.model} of model {vehicle.year} {type(vehicle).__name__}")
        vehicle.start_bike()
        vehicle.stop_bike()