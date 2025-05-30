class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        print("Initialization method")
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
         
    def set_number_served(self,people):  
        self.number_served = people
        print(f"Customer serverd: {self.number_served}") 
    
    def increment_number_served(self,people):
        self.number_served += people
        print(f"A day of bussiness: {self.number_served}") 

    
    
restaurant = Restaurant("Exotic","Mexican")
print(restaurant.number_served)
restaurant.number_served = 11
print(restaurant.number_served) 
restaurant.set_number_served(50)
restaurant.increment_number_served(25)