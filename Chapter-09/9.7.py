class User:

    def __init__(self,first_name,last_name,age, email):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.email=email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")



class Admin(User):
    def __init__(self,first_name,last_name,age, email,advantages):
        super().__init__(first_name,last_name,age, email)
        self.privileges = advantages
    def show_privileges(self):
        #print("Show --> {self.privileges}")
        print(self.privileges)


user1=User("Nafisa","Jui",22,"jui@gmail.com")

user1.describe_user()
adv=Admin("Nafisa","Jui",22,"jui@gmail.com",["can add post", "can delete post", "can ban user"])
adv.show_privileges()