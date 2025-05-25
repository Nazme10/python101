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


    def greet_user(self):
        print(f"Nice to meet you,{self.first_name} {self.last_name}!")

user1=User("Nafisa","Jui",22,"jui@gmail.com")
user2=User("Nazme","Rahman",21,"rahman10nazme@gmail.com")
user3=User("Ashfia","Shahreen",2,"ashIsSad@gmail.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

