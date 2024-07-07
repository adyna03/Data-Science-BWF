class Restaurant:
    def __init__(self, name, cuisine):
        self.name=name
        self.cuisine=cuisine

    def desc_rest(self):
        print(f"Restaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine}")

    def open_rest(self):
        print(f"{self.name} is now open!")

restaurant = Restaurant("The Happy Dragon", "Chinese")

print(f"Restaurant Name: {restaurant.name}")
print(f"Cuisine Type: {restaurant.cuisine}")

restaurant.desc_rest()
restaurant.open_rest()

