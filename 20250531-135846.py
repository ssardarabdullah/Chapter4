pizzas = ['pepperoni', 'margherita', 'bbq chicken', 'hawaiian', 'veggie', 'meat lovers']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")

# Slicing examples
print("\nThe first three items in the list are:")
print(pizzas[:3])

print("\nThree items from the middle of the list are:")
middle_index = len(pizzas) // 2
print(pizzas[middle_index - 1:middle_index + 2])

print("\nThe last three items in the list are:")
print(pizzas[-3:])