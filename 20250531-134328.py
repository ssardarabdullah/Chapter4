# Original menu as a tuple (immutable)
menu = ("Pizza", "Burger", "Pasta", "Salad", "Soup")

# Print each food item
print("Original Menu:")
for item in menu:
    print(item)
    # Create a new tuple with some items changed
menu = ("Sushi", "Burger", "Tacos", "Salad", "Ramen")

# Print revised menu
print("\nRevised Menu:")
for item in menu:
    print(item)
    #Original Menu:
Pizza
Burger
Pasta
Salad
Soup

#Revised Menu:
Sushi
Burger
Tacos
Salad
Ramen