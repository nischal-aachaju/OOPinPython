class User:
    def __init__(self,username,password,email):
        self.username=username
        self.__password=password
        self._email=email
    def change_password(self,password):
        self.__password=password
        return self.__password
    
user1=User("Nischal","123","nischal@gmail.com")
# print(user1._email)
print(user1.change_password("977"))
