class Users: 
    user_List = []
    
    user_name = ""    
    password = ""
    email = ""
    first_name = ""
    last_name = ""
    
    def create_user (self, user_name, password, email, first_name, last_name):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        
        new_User = {
            "Username" : self.user_name,
            "password" : self.password,
            "email" : self.email,
            "first_name" : self.first_name,
            "last_name" : self.last_name
        }
        self.user_List.append(new_User)
        return f" User {user_name} created. "
    
    def authentication(self, user_name, password):
        for user in self.user_List:
            if user["Username"] == user_name and user["password"] == password:
                return True
            else:
                return False
            
class signUpUser(Users):
    def signup(self):
        Username = input("\n Enter username: ")
        Password = input("\n Enter password: ")
        Email = input("\n Enter email: ")
        First_Name = input("\n Enter first Name: ")
        Last_Name = input("\n enter last Name: ")
        return self.create_user(Username, Password, Email, First_Name, Last_Name)
    
    def login(self):
        username = input("Enter UserName: ")
        password = input("Enter Password: ")
        if self.authentication(username, password):
            return f"User {username} logged in successfully."
        else: 
            return "Authentication failed. Invalid username or password."
        
    def show_user(self):
        for user in self.user_List:
            print(user)
            
user1 = signUpUser()
print(user1.signup())
user1.show_user()

print(user1.login())
