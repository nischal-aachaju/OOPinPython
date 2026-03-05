# this is class
# class Car:
#     color="blue"
#     model="an-453B"
#     type="engine"

# # this is object which defines the instances of class
# car1=Car()
# print(car1.color,car1.model,car1.type)

# car2=Car() 
# print(car2.color,car2.model,car2.type)

class Student:
    # # default constructure
    # def __init__(self):
    #     pass

    # parameterized constructure
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
s1=Student("nischal",18)
print(s1.name,s1.age)
s2=Student("nirjal",13)
print(s2.name,s2.age)