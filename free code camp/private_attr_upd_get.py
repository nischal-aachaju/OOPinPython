from datetime import datetime
class User:
    def __init__(self,username,password,email):
        self.username=username
        self.__password=password
        self._email=email
    def change_password(self,password):
        self.__password=password
        return self.__password
    
    def get_email(self):
        return self._email

    def set_email(self,new_email):
        try:
            if "@" not in new_email:
                raise Exception("invalid email")
            else:self._email=new_email
            
        except Exception as e:
            print(f"{e}")
        
user1=User("Nischal","123","nischal@gmail.com")
# print(user1._email)
# print(user1.change_password("977"))
# print(user1.get_email())
user1.set_email("hello@gmail.com")
print(f"Email is updatet at {datetime.now()}")
print(user1.get_email())

