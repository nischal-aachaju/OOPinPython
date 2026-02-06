_name="Nischal Shrestha"
_name=_name.lower().strip().split()
_name="_".join(_name)
print(_name)

password="Passion"
password=password.lower()
cleaner=password.maketrans("aeios","@#!0$")

clean_password=password.translate(cleaner)
print(clean_password)

dicts={"helo":"fg"}

print(type(dicts.keys()))
print(type(False))
print((True+True)&True)

a=list(range(1,4))
print(a)

print("{0}:{a}".format(0,a=12))

# a=complex(input("enter number"))
a=12+5j
print(a)
print(type(a))

a=-5

if a<-10:
    
    print("hge")
else:
    print("oiyt")
    
if not 1:
    print("D")
else:
    print("s")
    
import time

time.sleep(2)
print("SDf")
time.sleep(5)
print("etre")