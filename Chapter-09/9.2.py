class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        

restaurant1 = Restaurant("La Mirchi", "Continental")
restaurant2 = Restaurant("Exotic", "Mexican")
restaurant3 = Restaurant("Dae Jung Geum", "Korean")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
