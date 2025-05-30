class User:

    def __init__(self,first_name,last_name,age, email):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.email=email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")
        #print("attempts: {self.login_attempts}")
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"After reset: {self.login_attempts}")

user1=User("Nafisa","Jui",22,"jui@gmail.com")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

user1.reset_login_attempts()


