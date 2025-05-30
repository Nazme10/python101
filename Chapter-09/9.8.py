# User class represents a general user
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Nice to meet you, {self.first_name} {self.last_name}!")


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f" {privilege}")
        else:
            print("- This admin has no privileges assigned.")


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges(["can add post","can delete post","can ban user"])  


admin1 = Admin("Nazme", "Rahman", 21, "rahman10@gmail.com")
admin1.describe_user()
admin1.privileges.show_privileges()
