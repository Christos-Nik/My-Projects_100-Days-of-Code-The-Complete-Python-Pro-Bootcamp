class User:

    def __init__(self, user_id, username): #constructor function of a class
#        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        user.following += 1



user_1 = User("001", "angela")#assigns to the object class of User()
user_2 = User("002", "christos")
#attribute is a variable associated with an object
# user_1.id = "001" #assigns attribute of id to user_1
# user_1.username = "Christos" #assigns attribute of username to user_1

# print(f"User 1 ID: {user_1.id}\nUser 1 Username: {user_1.username}")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)