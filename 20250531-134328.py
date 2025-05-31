Question 2 ________
Use a for loop to print each food the restaurant offers.

•	 Try to modify one of the items, and make sure that Python rejects the 

change.

•	 The restaurant changes its menu, replacing two of the items with different 

foods. Add a line that rewrites the tuple, and then use a for loop to print 

each of the items on the revised menu.


solution _____


Original menu as a tuple (immutable)
menu = ("Pizza", "Burger", "Pasta", "Salad", "Soup")

  Print each food item
  print("Original Menu:")
for item in menu:
    print(item)
     Create a new tuple with some items changed
menu = ("Sushi", "Burger", "Tacos", "Salad", "Ramen")

 Print revised menu
print("\nRevised Menu:")
for item in menu:
    print(item)
    output_______
Pizza
Burger
Pasta
Salad
Soup

Revised Menu:
Sushi
Burger
Tacos
Salad
Ramen
