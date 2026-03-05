class Student:
    def __init__(self,name):
        self.name=name
        
    def hello(self):
        print(f"Hello!, {self.name}")

s1=Student("Nirjal")
print(s1.hello())