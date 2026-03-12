# inherantance

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        


class Car(Vehicle):
    
    def __init__(self,brand,model,year,number_of_doors,number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_doors=number_of_doors
        self.number_of_wheels=number_of_wheels
        
    def start_car(self):
        print("Vehicle is starting")
    def stop_car(self):
        print("Vehicle is stopping")

class Bike(Vehicle):
    def __init__(self,brand,model,year,number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_wheels=number_of_wheels

    def start_bike(self):
        print("Vehicle is starting")
    def stop_bike(self):
        print("Vehicle is stopping")

