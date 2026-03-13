# polymorphism


# if we dont apply polymorphism then---------------
# class Car():
    
#     def __init__(self,brand,model,year,number_of_doors,number_of_wheels):
#         self.brand=brand
#         self.model=model
#         self.year=year
#         self.number_of_doors=number_of_doors
#         self.number_of_wheels=number_of_wheels
        
#     def start_car(self):
#         print("car is starting")
#     def stop_car(self):
#         print("car is stopping")

# class Bike():
#     def __init__(self,brand,model,year,number_of_wheels):
#         self.brand=brand
#         self.model=model
#         self.year=year
#         self.number_of_wheels=number_of_wheels

#     def start_bike(self):
#         print("bike is starting")
#     def stop_bike(self):
#         print("bike is stopping")

# for vehicle in vehicles:
#     if isinstance(vehicle,Car):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} of model {vehicle.year} {type(vehicle).__name__}")
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle,Bike):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} of model {vehicle.year} {type(vehicle).__name__}")
#         vehicle.start()
#         vehicle.stop()

# -----------------------------------------------------

# if we apply polymorphism and inheritance then, we can make same program for more tham 2 Classes
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        
    def start(self):
        print("Vehicle is starting")
    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    
    def __init__(self,brand,model,year,number_of_doors,number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_doors=number_of_doors
        self.number_of_wheels=number_of_wheels

class Bike(Vehicle):
    def __init__(self,brand,model,year,number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_wheels=number_of_wheels


# list of vehicle to inspect
vehicles=[
    Car("Ford","Mustang",2009,4,4),
    Bike("BMW","S100RR",2022,2)

]


for vehicle in vehicles:
    if isinstance(vehicle,Vehicle):
         print(f"Inspecting {vehicle.brand} {vehicle.model} of model {vehicle.year} {type(vehicle).__name__}")
         vehicle.start()
         vehicle.stop()

