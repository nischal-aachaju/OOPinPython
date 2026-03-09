# static attribute
# it is used if the attributes are same for all the instances or like default attributes

class User:
    user_count=0
    def __init__(self,username,email):
        self._username=username
        self._email=email
        User.user_count +=1
    @staticmethod
    def hello():
        print(f"Hello user,")

user1=User("Nischal","nischal@gmail.com")
user2=User("Norman","norman@gmail.com")
print(User.user_count)
# print(user1._username) 
user1.hello()