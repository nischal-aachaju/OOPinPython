class Student:
    collage="Hello collage"
    name="anonymous" #class attributes
                                # object attributes> class attributes
    def __init__(self,name,marks):
        self.name=name # object attributes
        self.marks=marks
        print("adding new students in database.....")

s1=Student("Nischal",98)
print(s1.name)
