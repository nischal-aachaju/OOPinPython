class Student:
    # def __init__(self,name,mark1,mark2,mark3):
    #     self.name=name
    #     self.mark1=mark1
    #     self.mark2=mark2
    #     self.mark3=mark3
    def __init__(self,name,*mark):
        self.name=name
        self.total=sum(mark)
        
    def average_marks(self):
        average=self.total/3
        average=round(average,2)
        return average
    @staticmethod
    def hello():
        print("hello, students")
s1=Student("Nischal",96,91,90)
print(s1.name)
print(s1.average_marks())

s1.name="Nirjal"
print(s1.name)
print(s1.average_marks())

print(s1.hello())