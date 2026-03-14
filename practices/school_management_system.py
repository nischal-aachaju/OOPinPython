class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age >0:
            self.__age=age
            print(f"Age Updated. New age: {self.__age}")
        else:
            print("Invalid age")
    def __str__(self):
        return f"Name: {self.name}, Age: {self.get_age()}"
        
class Student(Person):
    
    def __init__(self, name, age,grade):
        self.grade=grade
        super().__init__(name, age)
            
    def study(self,subject):
        print(f"{self.name} is studying {subject}")
    def __str__(self):
        return f"{super().__str__()}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
    def __str__(self):
        return f"{super().__str__()}, Subject:{self.subject}" 
        

s1=Student("Nischal", 19, "Bachelor 1st year")
t1=Teacher("Norman",22,"Programing")
print(s1)
s1.study("Mathematices")
print(t1)
t1.teach()
s1.set_age(-10)
t1.set_age(30)