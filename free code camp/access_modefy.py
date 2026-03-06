class User:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password
        
    def say_hello_to_user(self,user):
        print(f"Message send to {user.username}: Hi, {user.username}. Its me {self.username}")

user1=User("Nischal","nischal@gmail.com","123")
user2=User("Ram","ram@gmail.com","123")

user1.say_hello_to_user(user2)

print(user1.email)
user1.email="nschal12@gmail.com"
print(user1.email)

