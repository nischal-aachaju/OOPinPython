from datetime import datetime
class User:
    def __init__(self,username,password,email):
        self.username=username
        self.__password=password
        self._email=email
    def change_password(self,password):
        self.__password=password
        return self.__password
    @property # this give access of function as a variable
    def email(self):
        return self._email

    @email.setter
    def email(self,new_email):
        self._email=new_email


user1=User("Nischal","123","nischal@gmail.com")
print(user1.email)
# print(type(user1.email))
user1.email="hello@gmail.com"
print(user1.email)