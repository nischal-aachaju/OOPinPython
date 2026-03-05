class Cat:
    def __init__(self,name,age,owner):
        self.name=name
        self.age=age
        self.owner=owner

class Owner:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact

owner1=Owner("nischal",9818)
owner2=Owner("Nirjal",123)
# print(owner1.name)

cat1=Cat("Miki",2,owner1)
cat2=Cat("Kiki",3,owner2)
print(cat1.owner.contact)
print(cat2.owner.name)

