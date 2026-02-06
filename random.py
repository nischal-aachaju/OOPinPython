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

