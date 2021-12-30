class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and they serve {self.cuisine_type} type of food")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now OPEN!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("\nWe have the following flavors available:")
        for item in self.flavors:
            print(item)


restaurant_cuisine = Restaurant("Paggoli", "Italian")

print(f"The restaurant's name is {restaurant_cuisine.restaurant_name}")
print(f"The restaurant serves {restaurant_cuisine.cuisine_type} cuisine!")
restaurant_cuisine.describe_restaurant()
restaurant_cuisine.open_restaurant()

big_one = IceCreamStand('The Big One', 'American')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.display_flavors()


