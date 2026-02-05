# data abstraction

class Car:
    def __init__(self):
        self.acc=False # data
        self.clutch=False # data
        self.brk=True # data
 
    def start(self):
        self.clutch=True # data
        self.acc=True # data
        print("Car is started ....")

car1=Car()
car1.start() # the internal process is hide. so, it is an abstraction which hide unnecessary data
