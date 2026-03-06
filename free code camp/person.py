class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def greed(self):
        print(f"Hello, My name is {self.name} and i am {self.age}")

p1=Person("Nischal",19)
p1.greed()
p2=Person("Nirjal",14)
p2.greed()