class Restaurant:
    def __init__(self, rest_name, cuisine):
        self.rest_name=rest_name
        self.cuisine=cuisine

    def desc_rest(self):
        print(f"Restaurant name: {self.rest_name}")
        print(f"Cuisine type: {self.cuisine}")

    def open_rest(self):
        print(f"{self.rest_name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, rest_name, cuisine="ice cream"):
        self.flavors = []  # Initialize empty list for flavors

    def set_flavors(self, flavors):
        super().__init__(rest_name, cuisine)
        self.flavors = flavors

    def display_flavors(self):
        print(f"\n{self.rest_name} offers these ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Cool Cones")

flavors = ["chocolate", "strawberry", "mint chip", "mango"]
ice_cream_stand.set_flavors(flavors)

ice_cream_stand.display_flavors()
