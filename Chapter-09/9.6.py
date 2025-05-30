class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
       
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
         
    def describe_restaurant(self):  
        print(f"This is the {self.restaurant_name} teahouse.") 
        print(f"It serves {self.cuisine_type} cuisine.")

    
    def open_restaurant(self):
       print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def display_flavors(self):
        for ice in self.flavors:
            print(ice)


restaurant = Restaurant("Exotic","Mexican")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

ice_cream = IceCreamStand("Exotic","Mexican",['chocolate','vanilla','matcha','honey','butterscotch'])
ice_cream.display_flavors()